import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

def crear_graficos():
    """
    Crea gráficos para todos los experimentos de búsqueda
    """
    
    # Crear directorio para gráficos
    if not os.path.exists('graficos'):
        os.makedirs('graficos')
    
    # Configurar estilo de gráficos
    plt.style.use('default')
    plt.rcParams.update({'font.size': 12})
    
    print("=== GENERANDO GRÁFICOS DE EXPERIMENTOS ===\n")
    
    # ========== EXPERIMENTO 1: EFECTO DEL TAMAÑO ==========
    print("1. Generando gráficos de efecto del tamaño...")
    
    # Leer datos de los tres algoritmos
    try:
        bin_tam = pd.read_csv('resultados/exp1_tam_bin.csv')
        seq_tam = pd.read_csv('resultados/exp1_tam_seq.csv') 
        gal_tam = pd.read_csv('resultados/exp1_tam_gal.csv')
        
        # Crear gráfico comparativo
        plt.figure(figsize=(12, 8))
        
        # Gráfico en escala logarítmica para mejor visualización
        plt.subplot(2, 2, 1)
        plt.loglog(bin_tam['Tamano'], bin_tam['Tiempo'], 'o-', label='Búsqueda Binaria', color='blue', linewidth=2)
        plt.loglog(seq_tam['Tamano'], seq_tam['Tiempo'], 's-', label='Búsqueda Secuencial', color='red', linewidth=2)
        plt.loglog(gal_tam['Tamano'], gal_tam['Tiempo'], '^-', label='Búsqueda Galloping', color='green', linewidth=2)
        plt.xlabel('Tamaño del Array (log)')
        plt.ylabel('Tiempo (nanosegundos, log)')
        plt.title('Comparación de Algoritmos: Tamaño vs Tiempo (Log-Log)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Gráfico en escala lineal
        plt.subplot(2, 2, 2)
        plt.plot(bin_tam['Tamano'], bin_tam['Tiempo'], 'o-', label='Búsqueda Binaria', color='blue', linewidth=2)
        plt.plot(gal_tam['Tamano'], gal_tam['Tiempo'], '^-', label='Búsqueda Galloping', color='green', linewidth=2)
        plt.xlabel('Tamaño del Array')
        plt.ylabel('Tiempo (nanosegundos)')
        plt.title('Búsqueda Binaria vs Galloping (Escala Lineal)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Gráfico solo secuencial para mostrar O(n)
        plt.subplot(2, 2, 3)
        plt.plot(seq_tam['Tamano'], seq_tam['Tiempo'], 's-', label='Búsqueda Secuencial', color='red', linewidth=2)
        plt.xlabel('Tamaño del Array')
        plt.ylabel('Tiempo (nanosegundos)')
        plt.title('Búsqueda Secuencial: Comportamiento O(n)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Gráfico de comparación normalizada
        plt.subplot(2, 2, 4)
        # Normalizar tiempos por el tamaño para mostrar complejidad
        bin_norm = bin_tam['Tiempo'] / np.log2(bin_tam['Tamano'])
        seq_norm = seq_tam['Tiempo'] / seq_tam['Tamano'] 
        gal_norm = gal_tam['Tiempo'] / np.log2(gal_tam['Tamano'])
        
        plt.plot(bin_tam['Tamano'], bin_norm, 'o-', label='Binaria / log(n)', color='blue', linewidth=2)
        plt.plot(seq_tam['Tamano'], seq_norm, 's-', label='Secuencial / n', color='red', linewidth=2)
        plt.plot(gal_tam['Tamano'], gal_norm, '^-', label='Galloping / log(n)', color='green', linewidth=2)
        plt.xlabel('Tamaño del Array')
        plt.ylabel('Tiempo Normalizado')
        plt.title('Análisis de Complejidad (Tiempo Normalizado)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('graficos/exp1_comparacion_tamanos.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("   ✓ Gráfico comparativo guardado: graficos/exp1_comparacion_tamanos.png")
        
    except Exception as e:
        print(f"   ✗ Error al procesar experimento 1: {e}")
    
    
    # ========== GRÁFICOS INDIVIDUALES ==========
    print("\n3. Generando gráficos individuales...")
    
    # Gráfico individual para cada algoritmo - Experimento 1
    for algoritmo, archivo, color in [('Binaria', 'bin', 'blue'), 
                                     ('Secuencial', 'seq', 'red'), 
                                     ('Galloping', 'gal', 'green')]:
        try:
            df = pd.read_csv(f'resultados/exp1_tam_{archivo}.csv')
            
            plt.figure(figsize=(10, 6))
            plt.plot(df['Tamano'], df['Tiempo'], 'o-', color=color, linewidth=2, markersize=8)
            plt.xlabel('Tamaño del Array')
            plt.ylabel('Tiempo (nanosegundos)')
            plt.title(f'Búsqueda {algoritmo}: Efecto del Tamaño')
            plt.grid(True, alpha=0.3)
            
            # Agregar línea de tendencia para secuencial
            if algoritmo == 'Secuencial':
                z = np.polyfit(df['Tamano'], df['Tiempo'], 1)
                p = np.poly1d(z)
                plt.plot(df['Tamano'], p(df['Tamano']), "--", alpha=0.7, 
                        label=f'Tendencia lineal: y = {z[0]:.2e}x + {z[1]:.1f}')
                plt.legend()
            
            plt.savefig(f'graficos/exp1_{archivo}_individual.png', dpi=300, bbox_inches='tight')
            plt.close()
            
            print(f"   ✓ Gráfico individual {algoritmo}: graficos/exp1_{archivo}_individual.png")
            
        except Exception as e:
            print(f"   ✗ Error en gráfico individual {algoritmo}: {e}")
    
    print("\n=== GRÁFICOS GENERADOS EXITOSAMENTE ===")
    print("\nArchivos creados en la carpeta 'graficos/':")
    print("- exp1_comparacion_tamanos.png (Comparación completa - Experimento 1)")
    print("- exp2_comparacion_posiciones.png (Comparación completa - Experimento 2)")
    print("- exp1_bin_individual.png (Búsqueda Binaria individual)")
    print("- exp1_seq_individual.png (Búsqueda Secuencial individual)")
    print("- exp1_gal_individual.png (Búsqueda Galloping individual)")
    print("\n¡Todos los gráficos están listos para el análisis!")

if __name__ == "__main__":
    crear_graficos()