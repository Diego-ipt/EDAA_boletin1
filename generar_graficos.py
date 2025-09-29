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
    
    # ========== EXPERIMENTO 2: EFECTO DE LA POSICIÓN ==========
    print("\n2. Generando gráficos de efecto de la posición...")
    
    try:
        bin_pos = pd.read_csv('resultados/exp2_pos_bin.csv')
        seq_pos = pd.read_csv('resultados/exp2_pos_seq.csv')
        gal_pos = pd.read_csv('resultados/exp2_pos_gal.csv')
        
        # Crear gráfico comparativo de posiciones
        plt.figure(figsize=(14, 10))
        
        # Gráfico principal: Posición vs Tiempo (ESCALA LOGARÍTMICA)
        plt.subplot(2, 2, 1)
        
        # Separar elementos encontrados y no encontrados
        bin_found = bin_pos[bin_pos['PosicionReal'] != -1]
        bin_not_found = bin_pos[bin_pos['PosicionReal'] == -1]
        
        seq_found = seq_pos[seq_pos['PosicionReal'] != -1]
        seq_not_found = seq_pos[seq_pos['PosicionReal'] == -1]
        
        gal_found = gal_pos[gal_pos['PosicionReal'] != -1]
        gal_not_found = gal_pos[gal_pos['PosicionReal'] == -1]
        
        # Plotear elementos encontrados con líneas en escala logarítmica
        plt.semilogy(bin_found['PosicionReal'], bin_found['Tiempo'], 
                    'o-', label='Binaria (Encontrados)', color='blue', linewidth=2, markersize=8)
        plt.semilogy(seq_found['PosicionReal'], seq_found['Tiempo'], 
                    's-', label='Secuencial (Encontrados)', color='red', linewidth=2, markersize=8)
        plt.semilogy(gal_found['PosicionReal'], gal_found['Tiempo'], 
                    '^-', label='Galloping (Encontrados)', color='green', linewidth=2, markersize=8)
        
        plt.xlabel('Posición Real en el Array')
        plt.ylabel('Tiempo (nanosegundos, escala log)')
        plt.title('Efecto de la Posición: Elementos Encontrados (Escala Logarítmica)')
        plt.legend()
        plt.grid(True, alpha=0.3)
        
        # Gráfico de elementos no encontrados (dividido en dos para claridad)
        # Subplot para Binaria y Galloping
        ax2 = plt.subplot(2, 2, 2)
        x_pos_bg = [1, 2]
        
        ax2.scatter([1]*len(bin_not_found), bin_not_found['Tiempo'], 
                   s=100, label='Binaria', color='blue', alpha=0.7, marker='o')
        ax2.scatter([2]*len(gal_not_found), gal_not_found['Tiempo'], 
                   s=100, label='Galloping', color='green', alpha=0.7, marker='^')
        
        ax2.set_xlabel('Algoritmo')
        ax2.set_ylabel('Tiempo (nanosegundos)')
        ax2.set_title('No Encontrados: Binaria vs Galloping')
        ax2.set_xticks(x_pos_bg)
        ax2.set_xticklabels(['Binaria', 'Galloping'])
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        # Subplot para Secuencial
        ax3 = plt.subplot(2, 2, 3)
        ax3.scatter([1]*len(seq_not_found), seq_not_found['Tiempo'], 
                   s=100, label='Secuencial', color='red', alpha=0.7, marker='s')
        
        ax3.set_xlabel('Algoritmo')
        ax3.set_ylabel('Tiempo (nanosegundos)')
        ax3.set_title('No Encontrados: Secuencial')
        ax3.set_xticks([1])
        ax3.set_xticklabels(['Secuencial'])
        ax3.legend()
        ax3.grid(True, alpha=0.3)
        
        # Formatear el eje Y para que sea más legible (notación científica)
        ax3.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        
        # Tabla resumen (SOLO TIEMPO MIN Y MAX)
        plt.subplot(2, 2, 4)
        plt.axis('off')
        
        # Crear tabla con estadísticas simplificadas
        estadisticas = [
            ['Algoritmo', 'Tiempo Min (ns)', 'Tiempo Max (ns)'],
            ['Binaria', f"{bin_pos['Tiempo'].min()}", f"{bin_pos['Tiempo'].max()}"],
            ['Secuencial', f"{seq_pos['Tiempo'].min()}", f"{seq_pos['Tiempo'].max()}"],
            ['Galloping', f"{gal_pos['Tiempo'].min()}", f"{gal_pos['Tiempo'].max()}"]
        ]
        
        table = plt.table(cellText=estadisticas[1:], colLabels=estadisticas[0],
                         cellLoc='center', loc='center', bbox=[0, 0, 1, 1])
        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1, 2.5)
        plt.title('Estadísticas Comparativas (Min-Max)')
        
        plt.tight_layout()
        plt.savefig('graficos/exp2_comparacion_posiciones.png', dpi=300, bbox_inches='tight')
        plt.close()
        
        print("   ✓ Gráfico de posiciones guardado: graficos/exp2_comparacion_posiciones.png")
        
    except Exception as e:
        print(f"   ✗ Error al procesar experimento 2: {e}")
    
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