import streamlit as st

def text_analyzer():
    st.title("📝 Text Analyzer")
    st.caption("A powerful tool to analyze and transform your text")

    # User Input with validation and placeholder
    text = st.text_area(
        "Enter your paragraph here:", 
        height=150,
        placeholder="Paste or type your text here...",
        help="This text will be analyzed when you submit"
    )
    
    # Submit button
    submitted = st.button("Analyze Text")
    
    if not submitted:  # Only show instructions if not submitted
        st.info("👆 Enter text and click the 'Analyze Text' button")
        return
    
    if not text.strip():
        st.warning("Please enter some text to analyze!")
        return
    
    # Text Analysis Features
    st.header("📊 Analysis Results", divider="rainbow")
    
    # Create columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        # Word and Character Count
        st.subheader("📝 Basic Stats")
        word_count = len(text.split())
        char_count = len(text)
        
        st.metric("Word Count", word_count)
        st.metric("Character Count (with spaces)", f"{char_count}")
        st.metric("Character Count (no spaces)", f"{len(text.replace(' ', ''))}")

    with col2:
        # Vowel and Consonant Count
        st.subheader("🔍 Text Insights")
        vowels = "aeiouAEIOU"
        vowel_count = sum(1 for char in text if char in vowels)
        
        st.metric("Vowel Count", vowel_count)
        st.metric("Consonant Count", sum(1 for char in text if char.isalpha() and char not in vowels))
        
        # Check for "Python"
        contains_python = "Python" in text or "python" in text
        st.metric("Contains 'Python'", "✅ Yes" if contains_python else "❌ No")

    # Average word length with visual
    if word_count > 0:
        avg_word_length = char_count / word_count
        st.subheader("📏 Word Length Analysis")
        
        mcol, vcol = st.columns([1, 3])
        with mcol:
            st.metric("Average Word Length", f"{avg_word_length:.1f} ", "chars")
        with vcol:
            st.progress(min(avg_word_length/10, 1.0), 
                        text=f"Visual scale (max 10 chars)")

    # Search and Replace
    st.subheader("🔍 Search & Replace", divider="rainbow")
    search_col, replace_col = st.columns(2)
    with search_col:
        search_word = st.text_input("Word to search:", placeholder="Enter word to find")
    with replace_col:
        replace_word = st.text_input("Replacement word:", placeholder="Enter replacement")
    
    if search_word:
        modified_text = text.replace(search_word, replace_word)
        st.text_area("Modified Text", modified_text, height=100)

    # Case Conversion
    st.subheader("🔄 Case Conversion", divider="rainbow")
    case_col1, case_col2 = st.columns(2)
    with case_col1:
        st.text("UPPERCASE:")
        st.code(f"{text.upper()}", language="text")
    with case_col2:
        st.text("lowercase:")
        st.code(f"{text.lower()}", language="text")

    # Additional features in expandable section
    with st.expander("📈 Advanced Analysis"):
        if word_count > 0:
            words = text.split()
            st.write(f"**Longest word:** '{max(words, key=len)}' ({len(max(words, key=len))} chars)")
            st.write(f"**Shortest word:** '{min(words, key=len)}' ({len(min(words, key=len))} chars)")
        st.write(f"**Sentence count:** {text.count('.') + text.count('!') + text.count('?')}")
        st.write(f"**Digit count:** {sum(1 for char in text if char.isdigit())}")

if __name__ == "__main__":
    text_analyzer()