# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.title("Youtube Downloader :smile:")

    st.subheader("Enter the link of the youtube video")
    query = st.text_input("")
    bt = st.button('Download')
    if bt:
        yt = YouTube(query)
        # Filter for audio stream
        audio_stream = yt.streams.filter(only_audio=True).first()
        # Download audio
        audio_stream.download(filename=f'{yt.title}.mp3')
        st.write("Audio downloaded!")
        st.audio(f"{yt.title}.mp3")

if __name__ == "__main__":
    run()
