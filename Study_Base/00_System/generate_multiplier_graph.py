
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import os

# Set japanese font if available, else standard sans-serif
# Try a few common Japanese fonts
plt.rcParams['font.family'] = ['Yu Gothic', 'Meiryo', 'MS Gothic', 'sans-serif']

def create_multiplier_graph(output_path):
    # Data for the graph
    Y = np.linspace(0, 100, 100)
    
    # 45-degree line (Y = AD)
    AD_supply = Y
    
    # Consumption function + Investment + Government Spending (Initial)
    # AD = C + I + G
    # Let C = cY + C0
    # AD = cY + (C0 + I + G)
    # Slope c (mpc) should be < 1. Let's say 0.6
    mpc = 0.6
    autonomous_1 = 20
    AD_1 = mpc * Y + autonomous_1
    
    # Increased Government Spending
    # AD' = C + I + G'
    delta_G = 10
    autonomous_2 = autonomous_1 + delta_G
    AD_2 = mpc * Y + autonomous_2
    
    # Calculate equilibrium points
    # Y = mpc * Y + A  =>  Y(1 - mpc) = A  =>  Y = A / (1 - mpc)
    Y1 = autonomous_1 / (1 - mpc)
    Y2 = autonomous_2 / (1 - mpc)
    
    AD1_at_Y1 = Y1
    AD2_at_Y2 = Y2

    # Plot
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # 45-degree line
    ax.plot(Y, AD_supply, 'k--', label='45度線 (Y=AD)', alpha=0.6)
    
    # AD curves
    ax.plot(Y, AD_1, 'b-', label='総需要 AD = C + I + G', linewidth=2)
    ax.plot(Y, AD_2, 'r-', label="総需要 AD' = C + I + G'", linewidth=2)
    
    # Equilibrium points
    ax.plot(Y1, AD1_at_Y1, 'bo', markersize=8)
    ax.plot(Y2, AD2_at_Y2, 'ro', markersize=8)
    
    # Drop lines to axes
    ax.vlines(Y1, 0, AD1_at_Y1, colors='b', linestyles='dotted', alpha=0.5)
    ax.vlines(Y2, 0, AD2_at_Y2, colors='r', linestyles='dotted', alpha=0.5)
    ax.hlines(AD1_at_Y1, 0, Y1, colors='b', linestyles='dotted', alpha=0.5)
    ax.hlines(AD2_at_Y2, 0, Y2, colors='r', linestyles='dotted', alpha=0.5)
    
    # Annotations
    ax.text(Y1, -5, '$Y_1$', color='b', ha='center', fontsize=12)
    ax.text(Y2, -5, '$Y_2$', color='r', ha='center', fontsize=12)
    
    ax.text(95, 95, '45°', rotation=45, ha='right', va='bottom')
    
    # Delta G arrow
    # Vertical arrow between AD1 and AD2 at some Y (e.g., Y1)
    arrow_x = Y1
    arrow_y_start = AD_1[int(Y1)] # essentially Y1 since Y1 is eq for AD1
    arrow_y_end = AD_2[int(Y1)]
    
    ax.annotate('', xy=(arrow_x, arrow_y_end), xytext=(arrow_x, arrow_y_start),
                arrowprops=dict(arrowstyle='<->', color='green', lw=1.5))
    ax.text(arrow_x - 2, (arrow_y_start + arrow_y_end)/2, r'$\Delta G$', color='green', va='center', ha='right', fontsize=12, fontweight='bold')

    # Delta Y arrow
    # Horizontal arrow on x-axis
    ax.annotate('', xy=(Y2, 5), xytext=(Y1, 5),
                arrowprops=dict(arrowstyle='->', color='purple', lw=1.5))
    ax.text((Y1 + Y2)/2, 8, r'$\Delta Y$', color='purple', ha='center', fontsize=12, fontweight='bold')
    
    # Labels
    ax.set_title('ケインズの乗数効果 (45度線分析)', fontsize=16)
    ax.set_xlabel('国民所得 (Y)', fontsize=14)
    ax.set_ylabel('総需要 (AD)', fontsize=14)
    
    # Limit ranges
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    
    # Grid
    ax.grid(True, linestyle=':', alpha=0.6)
    
    # Legend
    ax.legend(loc='upper left')
    
    # Hide axis ticks numbers if preferred, but keeping them gives scale context. 
    # Let's hide them for abstract theory feel
    ax.set_xticks([])
    ax.set_yticks([])
    
    # Remove top and right spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    plt.tight_layout()
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    plt.savefig(output_path, dpi=300)
    print(f"Graph saved to {output_path}")

if __name__ == '__main__':
    target_file = r'c:\Users\rikus\onedrive.kokurahunter\OneDrive\antigravity\Study_Base\01_Active_Courses\Schooling\2025_Autumn\Public_Finance_B\multiplier_effect.png'
    create_multiplier_graph(target_file)
