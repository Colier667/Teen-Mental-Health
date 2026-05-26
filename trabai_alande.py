import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Configurações estéticas para os slides
sns.set_theme(style="whitegrid")
plt.rcParams['figure.figsize'] = (16, 12)
plt.rcParams['font.size'] = 12

# 2. Carregamento do arquivo
df = pd.read_csv('Teen_Mental_Health_Dataset.csv', sep=';', decimal=',')

# Garantir que tudo que é número seja tratado como float/int de verdade
df['screen_time_before_sleep'] = df['screen_time_before_sleep'].astype(float)
df['sleep_hours'] = df['sleep_hours'].astype(float)
df['daily_social_media_hours'] = df['daily_social_media_hours'].astype(float)
df['stress_level'] = df['stress_level'].astype(int)
df['anxiety_level'] = df['anxiety_level'].astype(int)

# 3. Criando a matriz 2x2 para os 4 gráficos de dispersão modificados
fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# --- GRÁFICO 1: Tempo de Tela Noturno vs. Horas de Sono ---
# (Como ambas são contínuas, usamos jitter menor)
sns.regplot(data=df, x='screen_time_before_sleep', y='sleep_hours', 
            ax=axes[0, 0], color='royalblue', x_jitter=0.1, y_jitter=0.1,
            scatter_kws={'alpha':0.3, 's':25}, line_kws={'color':'red', 'linewidth': 3})
axes[0, 0].set_title('1. Tempo de Tela Noturno vs. Horas de Sono', fontsize=14, pad=10)
axes[0, 0].set_xlabel('Tempo de Tela Antes de Dormir (Horas)')
axes[0, 0].set_ylabel('Horas de Sono por Noite')

# --- GRÁFICO 2: Horas de Sono vs. Nível de Estresse ---
# (stress_level é inteiro de 1 a 10, então o jitter no eixo Y é essencial!)
sns.regplot(data=df, x='sleep_hours', y='stress_level', 
            ax=axes[0, 1], color='purple', x_jitter=0.1, y_jitter=0.2,
            scatter_kws={'alpha':0.3, 's':25}, line_kws={'color':'red', 'linewidth': 3})
axes[0, 1].set_title('2. Horas de Sono vs. Nível de Estresse', fontsize=14, pad=10)
axes[0, 1].set_xlabel('Horas de Sono por Noite')
axes[0, 1].set_ylabel('Nível de Estresse (1 a 10)')

# --- GRÁFICO 3: Uso Diário de Redes Sociais vs. Nível de Ansiedade ---
# (anxiety_level é inteiro de 1 a 10, jitter aplicado no eixo Y)
sns.regplot(data=df, x='daily_social_media_hours', y='anxiety_level', 
            ax=axes[1, 0], color='crimson', x_jitter=0.1, y_jitter=0.2,
            scatter_kws={'alpha':0.3, 's':25}, line_kws={'color':'darkred', 'linewidth': 3})
axes[1, 0].set_title('3. Horas de Redes Sociais vs. Nível de Ansiedade', fontsize=14, pad=10)
axes[1, 0].set_xlabel('Uso Diário de Redes Sociais (Horas)')
axes[1, 0].set_ylabel('Nível de Ansiedade (1 a 10)')

# --- GRÁFICO 4: Tempo de Tela Noturno vs. Nível de Ansiedade ---
sns.regplot(data=df, x='screen_time_before_sleep', y='anxiety_level', 
            ax=axes[1, 1], color='darkorange', x_jitter=0.1, y_jitter=0.2,
            scatter_kws={'alpha':0.3, 's':25}, line_kws={'color':'red', 'linewidth': 3})
axes[1, 1].set_title('4. Tempo de Tela Noturno vs. Nível de Ansiedade', fontsize=14, pad=10)
axes[1, 1].set_xlabel('Tempo de Tela Antes de Dormir (Horas)')
axes[1, 1].set_ylabel('Nível de Ansiedade (1 a 10)')

plt.tight_layout()
plt.savefig('graficos_dispersao_equipe8_fino.png', dpi=300)
plt.show()

# Print da correlação para garantir
print("\nMatriz de correlação atualizada:")
print(df[['screen_time_before_sleep', 'sleep_hours', 'daily_social_media_hours', 'stress_level', 'anxiety_level']].corr().round(3))