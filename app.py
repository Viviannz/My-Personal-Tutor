"""
Streamlit Web Interface for Personal Learning Tutor
Clean, professional interface with multi-provider support
"""

import streamlit as st
from tutor_agent import PersonalTutor

# Page configuration
st.set_page_config(
    page_title="Personal Learning Tutor",
    page_icon="🎓",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom CSS for clean, professional styling (NOT purple!)
st.markdown("""
    <style>
    /* Main theme colors - professional blue/gray */
    :root {
        --primary-color: #2E86AB;
        --background-color: #FFFFFF;
        --secondary-background: #F5F7FA;
        --text-color: #1F2937;
        --border-color: #E5E7EB;
    }

    /* Remove purple/pink default colors */
    .stButton > button {
        background-color: #2E86AB !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        padding: 0.5rem 2rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
    }

    .stButton > button:hover {
        background-color: #1a5a7a !important;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1) !important;
    }

    /* Clean input fields */
    .stTextInput > div > div > input {
        border: 2px solid #E5E7EB !important;
        border-radius: 8px !important;
        padding: 0.75rem !important;
    }

    .stTextInput > div > div > input:focus {
        border-color: #2E86AB !important;
        box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1) !important;
    }

    /* Chat messages */
    .user-message {
        background-color: #EBF5FB;
        border-left: 4px solid #2E86AB;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }

    .tutor-message {
        background-color: #F5F7FA;
        border-left: 4px solid #6B7280;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }

    /* Sidebar styling */
    .css-1d391kg {
        background-color: #F9FAFB !important;
    }

    /* Header styling */
    h1 {
        color: #1F2937 !important;
        font-weight: 700 !important;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Selectbox styling */
    .stSelectbox > div > div {
        border: 2px solid #E5E7EB !important;
        border-radius: 8px !important;
    }

    /* Text area */
    .stTextArea > div > div > textarea {
        border: 2px solid #E5E7EB !important;
        border-radius: 8px !important;
    }

    .stTextArea > div > div > textarea:focus {
        border-color: #2E86AB !important;
        box-shadow: 0 0 0 3px rgba(46, 134, 171, 0.1) !important;
    }
    </style>
    """, unsafe_allow_html=True)


def initialize_session_state():
    """Initialize Streamlit session state"""
    if 'tutor' not in st.session_state:
        st.session_state.tutor = None
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    if 'session_active' not in st.session_state:
        st.session_state.session_active = False


def render_message(role: str, content: str):
    """Render a chat message with custom styling"""
    if role == "user":
        st.markdown(f"""
        <div class="user-message">
            <strong>You:</strong><br>{content}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="tutor-message">
            <strong>🎓 Tutor:</strong><br>{content}
        </div>
        """, unsafe_allow_html=True)


def main():
    """Main application"""
    initialize_session_state()

    # Header
    st.markdown("# 🎓 Personal Learning Tutor")
    st.markdown("**Learn any topic fast with AI-powered guidance**")
    st.markdown("---")

    # Sidebar - Configuration
    with st.sidebar:
        st.markdown("## ⚙️ Settings")

        # Provider selection
        provider = st.selectbox(
            "Choose AI Provider",
            ["OpenAI", "Anthropic"],
            help="Select which AI service to use for tutoring"
        )

        # API Key input
        api_key = st.text_input(
            f"{provider} API Key",
            type="password",
            help=f"Enter your {provider} API key. Get one from {'platform.openai.com' if provider == 'OpenAI' else 'console.anthropic.com'}",
            placeholder=f"sk-..."
        )

        # Model selection (optional)
        if provider == "OpenAI":
            model_options = ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo"]
            default_model = "gpt-4o"
        else:
            model_options = ["claude-3-5-sonnet-20241022", "claude-3-opus-20240229", "claude-3-haiku-20240307"]
            default_model = "claude-3-5-sonnet-20241022"

        model = st.selectbox(
            "Model",
            model_options,
            index=0,
            help="Choose the AI model to use"
        )

        st.markdown("---")

        # Start/Reset session buttons
        if not st.session_state.session_active:
            if st.button("🚀 Start Learning Session", use_container_width=True):
                if not api_key:
                    st.error("⚠️ Please enter your API key first!")
                else:
                    try:
                        st.session_state.tutor = PersonalTutor(
                            provider=provider.lower(),
                            api_key=api_key,
                            model=model
                        )
                        st.session_state.session_active = True
                        st.session_state.messages = []

                        # Get initial greeting
                        initial_response = st.session_state.tutor.get_response(
                            "Hello! I'm ready to start learning."
                        )
                        st.session_state.messages.append(("tutor", initial_response))
                        st.rerun()
                    except Exception as e:
                        st.error(f"Error: {str(e)}")
        else:
            if st.button("🔄 Reset Session", use_container_width=True):
                st.session_state.tutor = None
                st.session_state.messages = []
                st.session_state.session_active = False
                st.rerun()

        # Info section
        st.markdown("---")
        st.markdown("### 📖 How It Works")
        st.markdown("""
        1. Enter your API key
        2. Start a learning session
        3. Tell the tutor what you want to learn
        4. Follow the step-by-step guidance
        5. Take action today!
        """)

        st.markdown("---")
        st.markdown("### 💡 Features")
        st.markdown("""
        - 80/20 focused learning
        - 4-hour action plans
        - Simple, clear explanations
        - Frequent comprehension checks
        - Practical, hands-on approach
        """)

    # Main chat area
    if not st.session_state.session_active:
        # Welcome screen
        st.markdown("""
        ### Welcome! 👋

        This AI tutor helps you learn **any topic** quickly and practically.

        **What makes this different?**
        - Focuses on the most useful 20% that gives 80% of results
        - Creates a 4-hour learning plan tailored to your goal
        - Uses plain language with everyday examples
        - Checks your understanding frequently
        - Helps you take action TODAY

        **To get started:**
        1. Choose your AI provider in the sidebar (OpenAI or Anthropic)
        2. Enter your API key
        3. Click "Start Learning Session"

        ---

        **Don't have an API key?**
        - OpenAI: [platform.openai.com](https://platform.openai.com)
        - Anthropic: [console.anthropic.com](https://console.anthropic.com)

        Both offer pay-as-you-go pricing. A typical learning session costs $0.10-0.50.
        """)

    else:
        # Display chat history
        for role, content in st.session_state.messages:
            render_message(role, content)

        # Chat input
        st.markdown("---")
        user_input = st.text_area(
            "Your message:",
            height=100,
            placeholder="Type your learning goals, questions, or responses here...",
            key="user_input"
        )

        col1, col2 = st.columns([1, 5])
        with col1:
            send_button = st.button("Send", use_container_width=True)

        if send_button and user_input.strip():
            # Add user message
            st.session_state.messages.append(("user", user_input))

            # Get tutor response
            with st.spinner("🤔 Tutor is thinking..."):
                try:
                    response = st.session_state.tutor.get_response(user_input)
                    st.session_state.messages.append(("tutor", response))
                except Exception as e:
                    st.error(f"Error: {str(e)}")

            st.rerun()


if __name__ == "__main__":
    main()
