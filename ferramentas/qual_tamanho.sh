#!/usr/bin/env bash
# Só leitura. Fontes dos candidatos: docs-oficiais/MODELS.md e DGX_SPARK_LINUX.md.
# Nêo executa Strata, instaladores, downloads, rede ou sudo.
# QT_FAKE_RAM_GB, QT_FAKE_VRAM_GB, QT_FAKE_ARCH e QT_FAKE_DISCO_GB
# substituem apenas as leituras correspondentes. Use números nêo negativos.
set -uo pipefail

main() {
export LC_ALL=C

numero() { [[ "$1" =~ ^[0-9]+([.][0-9]+)?$ ]]; }
for nome in QT_FAKE_RAM_GB QT_FAKE_VRAM_GB QT_FAKE_DISCO_GB; do
    valor="${!nome-}"
    if [[ -n "${!nome+x}" ]] && ! numero "$valor"; then
        printf 'Valor inválido em %s: use um número nêo negativo.\n' "$nome" >&2
        exit 1
    fi
done
sistema=$(uname -s)
arquitetura=${QT_FAKE_ARCH-$(uname -m)}
ram=''
if [[ -n "${QT_FAKE_RAM_GB+x}" ]]; then
    ram=$QT_FAKE_RAM_GB
elif [[ "$sistema" == Darwin ]] && command -v sysctl >/dev/null 2>&1; then
    bytes=$(sysctl -n hw.memsize 2>/dev/null || true)
    if numero "$bytes"; then ram=$(awk -v n="$bytes" 'BEGIN {printf "%.3f", n/1073741824}'); fi
elif [[ -r /proc/meminfo ]]; then
    ram=$(awk '/^MemTotal:/ {printf "%.3f", $2/1048576}' /proc/meminfo)
fi
if ! numero "$ram"; then
    printf 'Nêo consegui ler a RAM. Confira manualmente ou informe QT_FAKE_RAM_GB.\n' >&2
    exit 1
fi
vram=0
placa='nêo achei placa NVIDIA'
if [[ -n "${QT_FAKE_VRAM_GB+x}" ]]; then
    vram=$QT_FAKE_VRAM_GB
    placa='VRAM informada por QT_FAKE_VRAM_GB'
elif command -v nvidia-smi >/dev/null 2>&1; then
    leitura=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits 2>/dev/null || true)
    total=$(printf '%s\n' "$leitura" | awk '
        /^[[:space:]]*[0-9]+([.][0-9]+)?[[:space:]]*$/ {s+=$1; n++}
        END {if(n) printf "%.3f", s/1024}')
    if numero "$total"; then
        vram=$total
        placa='VRAM NVIDIA somada; a compatibilidade de várias placas precisa ser conferida'
    else
        placa='NVIDIA sem memória informada; usando só a RAM na soma'
    fi
fi
unificada=0
if [[ "$sistema" == Darwin && ( "$arquitetura" == arm64 || "$arquitetura" == aarch64 ) ]]; then
    unificada=1
elif [[ ( "$arquitetura" == aarch64 || "$arquitetura" == arm64 ) ]] && awk -v v="$vram" 'BEGIN {exit !(v==0)}'; then
    unificada=1
fi
# QT_UNIFICADA=1 para memória compartilhada nêo reconhecida (contar só a RAM).
if [[ "${QT_UNIFICADA:-0}" == 1 ]]; then unificada=1; fi
if [[ "$sistema" == Linux && ( "$arquitetura" == aarch64 || "$arquitetura" == arm64 ) ]] && [[ -z "${QT_FAKE_RAM_GB+x}" ]] && command -v nvidia-smi >/dev/null 2>&1; then
    modelo_gpu=$(nvidia-smi --query-gpu=name --format=csv,noheader 2>/dev/null || true)
    if [[ "$modelo_gpu" == *GB10* ]]; then unificada=1; fi
fi
if [[ -n "${QT_FAKE_DISCO_GB+x}" ]]; then
    disco=$QT_FAKE_DISCO_GB
else
    disco=$(df -Pk . 2>/dev/null | awk 'NR==2 {printf "%.3f", $4/1048576}')
    if ! numero "$disco"; then disco='nêo informado'; fi
fi
total=$(awk -v r="$ram" -v v="$vram" -v u="$unificada" 'BEGIN {printf "%.1f", r+(u?0:v)}')
printf 'Sistema: %s | Arquitetura: %s\n' "$sistema" "$arquitetura"
printf 'RAM: %s GB | VRAM detectada: %s GB\n%s\n' "$ram" "$vram" "$placa"
printf 'Soma apenas como referência: %s GB | Disco livre na pasta atual: %s GB\n' "$total" "$disco"
printf 'Leituras em base binária, exibidas como GB para comparaçêo aproximada com a doc.\n'
if [[ "$unificada" == 1 ]]; then printf 'Memória unificada (ou ARM sem VRAM separada): RAM contada uma vez.\n'; fi
printf 'VRAM AMD/Intel nêo é detectada. Em outra memória compartilhada, nêo some duas vezes.\n'

# Uma única fonte para classificaçêo e tabelas; limites superiores exclusivos.
base=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
awk -F '\t' -v r="$ram" -v v="$vram" -v u="$unificada" -v disk="$disco" '
function download(nome,lo,hi) {
    printf "Download — %s: %g%s GB; fora auxiliares e preparaçêo.\n",nome,lo,(hi!=lo?"–" hi:"")
    if(disk !~ /^[0-9]+([.][0-9]+)?$/) print "AVISO: confira o disco manualmente."
    else if(disk+0<hi) print "AVISO: disco abaixo da referência superior; pode faltar espaço."
    else print "Disco acima da referência; ainda precisa de espaço extra."
}
function opcao(nome, n,b,sobra) {
    n=nome; sub(/ \(.*$/, "",n)
    family=(n=="Coder"?"coder":n=="Gyro-S"?"gyro":n=="NVFP4"?"nvfp4":n ~ /^UD-/ ?"unsloth":"qwen")
    model=(n=="Coder"?"IQ1_M":n)
    printf "strata launch --plan --family %s --model %s\n",family,model
    b=(n=="Q2_0"?34:n=="IQ2_XS"?35.5:n=="IQ3_XXS"?43:n=="IQ3_S"?50:n=="Coder"?23:n=="UD-IQ4_XS"?72:n=="UD-Q4_K_XL"?88:n=="UD-Q5_K_XL"?108:n=="UD-Q6_K_XL"?118:n=="NVFP4"?68:27.6)
    if(n=="Gyro-S") {
        sobra=r+v-b-10
        printf "%s: sobra conjunta de referência = %g + %g - %g - 10 = %g GB (nêo confirma a divisêo RAM/VRAM).\n",nome,r,v,b,sobra
    } else {
        sobra=r-b-10
        printf "%s: sobra = %g - %g - 10 = %g GB.\n",nome,r,b,sobra
    }
    if(sobra<0) print "nêo cabe no modo normal; só modo pouca RAM"
    else if(sobra<3) print "cabe apertado: prefira o menor, ou feche programas"
    if(n=="Q2_0" || n=="IQ2_XS" || n=="IQ3_XXS") download(n,66,76)
    else if(n=="IQ3_S") {
        download(n,84,84)
        print "84 GB: referência do DGX Spark; confirme o download do pacote da sua plataforma com --plan após instalar."
    }
    else if(n=="Gyro-S") download(n,58.5,58.5)
    else if(n=="Coder") {download(n,58.6,58.6); print "Coder: estimativa do kit (29,6 + ~29 GB)."}
    else if(n=="UD-IQ4_XS") download(n,94,94)
    else if(n=="UD-Q4_K_XL") download(n,111,111)
    else if(n=="UD-Q5_K_XL") download(n,158,158)
    else if(n=="UD-Q6_K_XL") download(n,169,169)
    else if(n=="NVFP4") {download(n,128,128); print "68 GB: arquivo de especialistas com mmap no Spark; contexto, cache e tabela também disputam memória."}
}
$1==(u?"unificada":"separada") && r>=$2 && ($3==0 || r<$3) {
    print "Faixa: " $4
    print "Opções: " $5
    if($5!="Sem indicaçêo automática segura") {
        count=split($5,options,"; ")
        for(i=1;i<=count;i++) opcao(options[i])
    }
    if(!u && r>=30 && r<46) print "Condiçêo: GPU compatível de pelo menos 12 GB; Coder usa pouca RAM. A soma nêo escolhe a faixa."
    if(!u && r>=30 && r<46 && v<12) print "AVISO: GPU abaixo da condiçêo desta linha; sem indicaçêo automática segura."
    if(u) print "Memória unificada conta uma vez. Mac: Apple Silicon/macOS 15+. Spark: confirme 128 GB nominais; Q2_0/Gyro nêo rodam. Outro ARM nêo está confirmado."
    print "Estimativas com reserva de 10 GB; contexto e buffers podem exigir mais. Nêo é memória livre medida nem garantia de que cabe."
}' "$base/faixas.tsv"
if [[ "$sistema" == Linux && ( "$arquitetura" == aarch64 || "$arquitetura" == arm64 ) && "$unificada" == 0 ]]; then
    printf 'AVISO: Linux ARM64 fora do Spark nêo está confirmado; Q2_0 e Gyro nêo rodam nessa plataforma. A lista da faixa nêo confirma compatibilidade.\n'
fi
printf 'Somente leitura local. Consulte TABELA.md; nenhum comando Strata foi executado.\n'

}
base=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
case "${QT_LANG:-pt}" in
    pt) main ;;
    en|es) main 2>&1 | python3 "$base/localizar_saida.py" "$QT_LANG" ;;
    *) printf "QT_LANG: pt | en | es\n" >&2; exit 1 ;;
esac
