#!/bin/bash
 HEAD
echo "Simulación MORCE-QFT iniciada"
# Aquí iría la lógica del script


# Parámetros por defecto
EEG_PATH="demo"
TRIALS=1000
T_MAX=12.0
MEM_STRENGTH=0.18

# Procesar argumentos
while [[ $# -gt 0 ]]; do
    case "$1" in
        --eeg_path)
        EEG_PATH="$2"
        shift 2
        ;;
        --trials)
        TRIALS="$2"
        shift 2
        ;;
        --t_max)
        T_MAX="$2"
        shift 2
        ;;
        --mem_strength)
        MEM_STRENGTH="$2"
        shift 2
        ;;
        *)
        shift
        ;;
    esac
done

echo "🚀 Iniciando Pipeline MORCE-QFT de Giovanni Juárez Herrera"
echo "▸ EEG: $EEG_PATH"
echo "▸ Trials: $TRIALS"
echo "▸ t_max: $T_MAX"
echo "▸ Memoria topológica: $MEM_STRENGTH"

python pipelines/morce_pipeline.py \
    --eeg_path "$EEG_PATH" \
    --trials $TRIALS \
    --t_max $T_MAX \
    --mem_strength $MEM_STRENGTH

echo "✅ Pipeline completado! Ver resultados en:"
echo "- morce_results.png"
echo "- morce_metrics_report.txt"
 0ef36fc (ADD: run_pipeline script)
