import streamlit as st
import openai
openai.api_key = "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"


def get_answer(prompt):
    full_prompt = f"I am Advanced ChatGPT ✈️, a language model developed by Alpha. I'm here to help answer your questions and engage in conversation on a wide range of topics. Is there something specific you would like to know or discuss?.\n\nQ: {prompt}\nA:"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=full_prompt,
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n"]
    )
    answer = response.choices[0].text.strip()
    return answer


def create_image(prompt):
    response = openai.Image.create(
        
        
        
        n=2,
        
        prompt=prompt,
        
         
    )
    image_url = response['data'][0]['url']
    return image_url


st.title("Advanced ChatGPT ✈️")
st.subheader("Ask a question or generate an image")

user_input = st.text_input("Type your question or enter 'generate image' to create an image", key="input")

if user_input:
    if user_input.lower() == "generate image":
        image_prompt = st.text_input("Enter the image prompt", key="image_prompt")
        
        if image_prompt:
            with st.spinner("Generating image..."):
                image_url = create_image(image_prompt)
            st.success("Image generated successfully!")
           
            st.image(image_url, width=400)  # Adjust the width as per your preference
            st.button("Generate more")
    else:
        answer = get_answer(user_input)
        st.write("Q:", user_input)
        st.write("A:", answer)
