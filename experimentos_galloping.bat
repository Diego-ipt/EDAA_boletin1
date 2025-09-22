@echo off
setlocal enabledelayedexpansion
echo =====================================================
echo EXPERIMENTOS PARA ANALISIS DE BUSQUEDA GALLOPING
echo =====================================================
echo.

REM Crear directorio para resultados
if not exist "resultados" mkdir resultados

echo EXPERIMENTO 1: Efecto del tamano de la secuencia
echo =================================================
echo Ejecutando busquedas en diferentes tamanos de array...
echo.

REM Experimento 1: Efecto del tamaño (posición fija en el medio - posición 3)
echo Tamano,Tiempo,PosicionEncontrada > resultados\exp1_tam_gal.csv
echo Usando posicion 3 (elemento en el medio del array)

for %%s in (1024 2048 4096 8192 16384 32768 65536 131072 262144 524288 1048576) do (
    echo Procesando tamano %%s...
    for /f "tokens=1,2" %%a in ('gallopingS.exe data/data_size_%%s.txt 3') do (
        echo %%s,%%a,%%b >> resultados\exp1_tam_gal.csv
    )
)

echo.
echo EXPERIMENTO 2: Efecto de la posicion del elemento
echo =================================================
echo Ejecutando busquedas en diferentes posiciones (tamano fijo: 1048576)...
echo.

REM Experimento 2: Efecto de la posición (tamaño fijo - archivo más grande)
echo PosicionReal,Tiempo,PairUsado > resultados\exp2_pos_gal.csv
echo Usando archivo data_size_1048576.txt

REM Posiciones 0-6: elementos que existen en diferentes posiciones
REM Posiciones 7-9: elementos que no existen
for /L %%i in (0,1,9) do (
    echo Procesando pair %%i...
    for /f "tokens=1,2" %%a in ('gallopingS.exe data/data_size_1048576.txt %%i') do (
        echo %%b,%%a,%%i >> resultados\exp2_pos_gal.csv
    )
)

echo.
echo =====================================================
echo EXPERIMENTOS COMPLETADOS
echo =====================================================
echo.
echo Resultados guardados en:
echo - resultados\exp1_tam_gal.csv
echo - resultados\exp2_pos_gal.csv
echo.
echo EXPERIMENTO 1: Analiza como varia el tiempo con el tamano del array
echo EXPERIMENTO 2: Analiza como varia el tiempo con la posicion del elemento
echo.
echo Para crear graficos:
echo - Eje X (Exp 1): Tamano del array (1024 a 1048576)
echo - Eje Y (Exp 1): Tiempo de ejecucion (nanosegundos)
echo - Eje X (Exp 2): Posicion real del elemento
echo - Eje Y (Exp 2): Tiempo de ejecucion (nanosegundos)
echo.
echo NOTA: La busqueda galloping tiene complejidad O(log n)
echo      Optimizada para elementos cercanos al inicio
echo.
