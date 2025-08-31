
## Código Flask removido. Apenas Streamlit abaixo.
import streamlit as st

st.set_page_config(page_title="Mundo Stevia - Saúde em Foco", layout="wide")

menu = [
    "Bem-vindo",
    "O que é Stevia",
    "Benefícios",
    "Efeitos Adversos",
    "Segurança",
    "Comparação",
    "Conclusão"
]

st.sidebar.title("Mundo Stevia - Saúde em Foco")
page = st.sidebar.radio("Navegação", menu)

if page == "Bem-vindo":
    st.title("Bem-vindo ao Mundo Stevia - Saúde em Foco")
    st.image("static/img/foto1.webp", use_container_width=True, caption="Stevia e saúde")
    st.markdown("""
    Descubra como a stevia pode transformar sua saúde! A stevia é um adoçante natural, sem calorias, ideal para quem busca uma vida mais saudável.
    """)
    st.button("Saiba mais", on_click=lambda: st.experimental_rerun())

elif page == "O que é Stevia":
    st.header("O que é Stevia")
    st.markdown("""
    A Stevia rebaudiana Bertoni é um adoçante natural derivado das folhas de uma planta nativa do Paraguai, conhecida por seu sabor extremamente doce e por não fornecer calorias significativas. Os compostos adoçantes da estévia são os glicosídeos de esteviol, especialmente esteviosídeo e rebaudiosídeo A, substâncias até 400 vezes mais doces que o açúcar de mesa.
    
    Devido ao alto poder adoçante, apenas pequenas quantidades de estévia são necessárias para adoçar alimentos e bebidas, permitindo substituir o açúcar comum sem aumentar a ingestão calórica. Inicialmente utilizada por povos indígenas e popularizada no Japão, a estévia ganhou aprovação internacional como alternativa natural aos adoçantes artificiais e ao açúcar tradicional.
    
    O uso da estévia é recomendado para quem busca uma alimentação mais saudável, redução de calorias e controle da glicemia. O adoçante é aprovado por órgãos reguladores como FDA, EFSA e Anvisa, sendo considerado seguro para consumo humano.
    """)

elif page == "Benefícios":
    st.header("Benefícios da Stevia")
    st.markdown("""
    - **Zero calorias:** adoça sem adicionar calorias à dieta, auxiliando em dietas de emagrecimento ou manutenção de peso.
    - **Não eleva a glicemia:** seguro para diabéticos e pessoas com resistência à insulina.
    - **Origem natural:** extraída da planta Stevia rebaudiana, utilizada há séculos por povos indígenas.
    - **Não causa cáries:** não é fermentada pelas bactérias da boca, ajudando a prevenir cáries e problemas gengivais.
    - **Rica em antioxidantes:** compostos naturais que podem conferir propriedades antioxidantes e anti-inflamatórias.
    - **Possível redução da pressão arterial:** estudos sugerem efeito benéfico em hipertensos.
    - **Adequada para dietas especiais:** indicada para diabéticos, pessoas com síndrome metabólica, hipertensos e portadores de fenilcetonúria.
    
    Além dos benefícios principais, pesquisas iniciais indicam que a estévia pode ter efeitos positivos no trato digestivo, imunidade e saúde renal, embora esses efeitos ainda estejam em investigação.
    """)

elif page == "Efeitos Adversos":
    st.header("Efeitos Adversos e Riscos")
    st.markdown("""
    - Geralmente segura e bem tolerada, sem efeitos colaterais relevantes em uso moderado.
    - Em excesso, pode causar desconfortos gastrointestinais leves, como náusea, gases, distensão abdominal e diarreia, especialmente em produtos mistos com polióis.
    - Leve efeito hipotensor: pode reduzir discretamente a pressão arterial, sendo benéfico para hipertensos, mas requer atenção em pessoas com pressão baixa.
    - Raramente causa alergias; atenção para pessoas sensíveis à família Asteraceae.
    - Não há evidências de efeitos hormonais ou reprodutivos negativos em humanos dentro das doses recomendadas.
    - Não há interações medicamentosas graves documentadas, mas diabéticos e hipertensos devem monitorar seus tratamentos ao introduzir estévia regularmente.
    
    A ingestão diária aceitável (IDA) é de 4 mg/kg de peso corporal por dia, valor raramente ultrapassado em condições normais. O uso moderado é considerado seguro para a maioria das pessoas.
    """)

elif page == "Segurança":
    st.header("Segurança segundo órgãos reguladores")
    st.markdown("""
    A segurança da estévia foi avaliada por diversas agências regulatórias e comitês científicos internacionais. FDA (EUA), EFSA (Europa) e Anvisa (Brasil) consideram a estévia segura para consumo humano dentro dos limites recomendados, não apresentando toxicidade genotóxica, carcinogênica ou riscos à reprodução.
    
    A Ingestão Diária Aceitável (IDA) é de 4 mg/kg de peso corporal por dia, valor raramente ultrapassado em condições normais. Estudos toxicológicos e epidemiológicos mostram ampla margem de segurança, sem evidência de toxicidade acumulativa, mesmo em países onde a estévia é consumida em larga escala.
    
    No Brasil, a Anvisa incentiva o uso da estévia como alternativa ao açúcar para diabéticos e demais consumidores, dentro de uma alimentação equilibrada. A pureza dos produtos é regulamentada, garantindo segurança ao consumidor.
    """)

elif page == "Comparação":
    st.header("Comparação com Outros Adoçantes")
    st.markdown("""
    - **Comparação com açúcar:** Stevia não contém calorias nem carboidratos assimiláveis, não eleva a glicemia e não causa cáries, sendo mais saudável que o açúcar tradicional.
    - **Comparação com adoçantes naturais:** Stevia e polióis (xilitol, eritritol) não elevam a glicose, mas polióis podem causar desconfortos intestinais em excesso. Stevia tem poder adoçante muito superior.
    - **Comparação com adoçantes artificiais:** Stevia é considerada natural, enquanto aspartame, sucralose e sacarina são sintéticos. Todos são seguros em moderação, mas a stevia não possui restrições metabólicas específicas.
    - A escolha entre adoçantes depende do gosto, objetivo e contexto de saúde. Stevia pode ter leve amargor residual, enquanto outros adoçantes variam em sabor e estabilidade térmica.
    - Todos os adoçantes aprovados são considerados seguros pelas autoridades reguladoras, desde que usados dentro das recomendações.
    
    Nenhum adoçante é solução mágica para a saúde. Moderação e dieta equilibrada continuam sendo fundamentais.
    """)

elif page == "Conclusão":
    st.header("Resumo Final")
    st.markdown("""
    A estévia emergiu como um importante aliado na redução do consumo de açúcar, oferecendo dulçor intenso sem calorias e com impacto negligenciável na glicemia. Os benefícios potenciais incluem melhor controle do açúcar no sangue, auxílio no controle de peso (quando usada para substituir o açúcar em uma dieta equilibrada), segurança para diabéticos e não contribui para problemas dentários.
    
    Pesquisas sugerem efeitos positivos extras, como propriedades antioxidantes e ligeira redução de pressão em hipertensos, embora tais efeitos ainda estejam em investigação. Os riscos e efeitos adversos da estévia se mostraram mínimos: a maioria dos estudos não detecta efeitos nocivos significativos dentro das doses usuais. Alguns indivíduos podem experimentar desconfortos gastrointestinais leves ou alterações de paladar, geralmente por consumo excessivo ou sensibilidade individual.
    
    Órgãos de saúde de renome mundial – FDA (EUA), EFSA (Europa) e Anvisa (Brasil) – analisaram extensivamente a segurança da estévia e concluíram que o adoçante é seguro para consumo humano, não causando câncer, mutações genéticas ou danos reprodutivos dentro da ingestão diária aceitável. A IDA típica de 4 mg/kg fornece uma margem confortável, e dificilmente alguém ultrapassa esse limite em condições normais.
    
    Em comparação com outros adoçantes, a estévia apresenta vantagens de ser natural e sem calorias, equiparando-se aos adoçantes artificiais na eficácia em adoçar sem elevar a glicose. Todos os adoçantes aprovados são seguros em moderação, e a escolha depende de preferências de sabor ou objetivos específicos. Nenhum adoçante é solução mágica para a saúde – moderação e dieta equilibrada continuam fundamentais.
    
    Para quem busca diminuir o açúcar sem abrir mão do paladar doce, a estévia desponta como uma das melhores alternativas disponíveis, unindo tradição natural e validação científica moderna. Em suma, o adoçante de estévia oferece uma forma de adoçar a vida com menos preocupações de saúde, desde que usado com bom senso e dentro dos limites recomendados.
    """)
