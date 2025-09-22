@echo off
echo =====================================================
echo GENERADOR DE GRAFICOS PARA EXPERIMENTOS DE BUSQUEDA
echo =====================================================
echo.

echo Verificando Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no encontrado. Por favor instale Python primero.
    echo Descargue desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python encontrado correctamente.
echo.

echo Instalando dependencias necesarias...
echo Instalando pandas...
pip install pandas

echo Instalando matplotlib...
pip install matplotlib

echo Instalando numpy...
pip install numpy

echo.
echo =====================================================
echo GENERANDO GRAFICOS...
echo =====================================================
echo.

echo Ejecutando generador de graficos...
python generar_graficos.py

echo.
echo =====================================================
echo PROCESO COMPLETADO
echo =====================================================
echo.

echo Los graficos han sido generados en la carpeta 'graficos/'
echo.
echo Archivos creados:
echo - exp1_comparacion_tamanos.png
echo - exp2_comparacion_posiciones.png  
echo - exp1_bin_individual.png
echo - exp1_seq_individual.png
echo - exp1_gal_individual.png
echo.

if exist "graficos" (
    echo Abriendo carpeta de graficos...
    start graficos
) else (
    echo ADVERTENCIA: La carpeta 'graficos' no fue creada.
    echo Verifique que no haya errores en la ejecucion.
)

echo.