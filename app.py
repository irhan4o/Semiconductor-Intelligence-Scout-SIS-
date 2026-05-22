import streamlit as st
import urllib.parse
import re

# Прост уеб интерфейс за контролния ти панел
st.set_page_config(page_title="SIS - Semiconductor Intel Scout", layout="centered")
st.title("📡 Semiconductor Intel Scout")

query = st.text_input(
    "Въведи заявка за разузнаване:", 
    value="what were the latest in-person events in South Korea on photovoltaics?"
)
country = st.selectbox(
    "Избери целева държава:", 
    ["South Korea", "Taiwan", "Netherlands", "Japan", "US", "China", "Germany", "France"]
)

country_domains = {
    "South Korea": "site:.kr",
    "Taiwan": "site:.tw",
    "Netherlands": "site:.nl",
    "Japan": "site:.jp",
    "US": "site:.gov OR site:.edu",
    "China": "site:.cn",
    "Germany": "site:.de",
    "France": "site:.fr"
}

if st.button("Стартиране на разузнаването"):
    import ollama
    
    st.info(f"🤖 Локалният модел (Llama 3) обработва заявката...")
    
    # Супер строг промпт с пример (Few-shot prompting), за да спрем бърборенето на модела
    prompt = (
        f"Task: Translate the search query into the primary language of {country}.\n"
        f"Query: '{query}'\n"
        f"Instruction: Output ONLY the final raw translation. "
        f"DO NOT include 'Note:', DO NOT include English explanations, DO NOT use parentheses, DO NOT repeat the prompt. "
        f"Just the translated text."
    )
    
    try:
        response = ollama.generate(model="llama3", prompt=prompt)
        raw_output = response['response'].strip()
        
        # 🛡️ ПОЧИСТВАНЕ: Премахваме кавички, скоби и системни съобщения от типа на (Note: ...)
        clean_query = re.sub(r'\(.*?\)', '', raw_output) # Маха всичко в скоби
        clean_query = re.sub(r'(Note|Translation):.*', '', clean_query, flags=re.IGNORECASE) # Маха "Note:"
        clean_query = clean_query.replace('"', '').replace("'", "").strip()
        
        # Ако моделът е върнал празен низ заради почистването, слагаме оригиналната заявка като спасителен вариант
        if not clean_query:
            clean_query = query

        st.subheader("📋 Резултати от агента:")
        st.write(f"**Преведена заявка (Native):** `{clean_query}`")
        
        # Сглобяваме интелигентната търсачка
        domain_filter = country_domains[country]
        full_search_query = f"{clean_query} {domain_filter}"
        
        # Кодираме правилно за уеб линк
        encoded_query = urllib.parse.quote(full_search_query)
        search_url = f"https://html.duckduckgo.com/html/?q={encoded_query}"
        
        st.success("✅ Локалният превод завърши успешно и данните бяха филтрирани!")
        st.write("---")
        st.write(f"ℹ️ Нов, изчистен линк за интелигентно разузнаване в {country}:")
        
        st.markdown(f"### 🔗 [Кликни тук за достъп до чистите резултати]({search_url})")
        
    except Exception as e:
        st.error(f"Връзката с Ollama пропадна: {e}. Увери се, че приложението Ollama работи на заден план.")