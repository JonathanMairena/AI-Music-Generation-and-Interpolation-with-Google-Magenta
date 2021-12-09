# CIS519: AI Music Generation and Interpolation with Google Magenta

For this project, we explored the idea of AI generated music using two models, MelodyRNN and MusicVAE, from Google Magenta. Using AI to generate music can aid music creators with creativity and enhance song generation by providing a tool for sampling and altering their favorite songs. Our primary target contribution is in using a new training dataset for the two models. We trained our models using piano-only MIDI data from 909 pop songs from the POP909 dataset for 1) music generation and 2) music interpolation, respectively. We extensively preprocessed the data to output a format that was compatible with the Google Magenta models and then used this processed data to train our models. We varied the number of steps when training each of the MelodyRNN models, with the 1,000-step model achieving 52% accuracy and 4.58 perplexity, after training for 36 minutes, and the 20,000-step model achieving 58% accuracy and 3.67 perplexity, after training for 10 hours. For the MusicVAE model, we were able to achieve an ending loss of 2.9 with a starting loss of 144.1, after training the model for 2 hours. We then outputted the results using a test set of the data and compared the results from the trained model to the pretrained Magenta model. 

**Data Processing:** Contains all files related to pre-processing the POP909 data set

**Melody RNN 1k:** Google Colab notebook containing code related to training and outputting results of the Melody RNN model of 1,000 steps

**Melody RNN 20k:** Google Colab notebook containing code related to training and outputting results of the Melody RNN model of 20,000 steps

**MusicVAE Interpolate 2bar:** Google Colab notebook containing code related to training and outputting results of the MusicVAE model for interpolating 2 bars of music

**Medium article:** https://medium.com/@jmairena/ai-music-generation-and-interpolation-9f49e50722ec

**Full Set of Melody RNN Results:** https://soundcloud.com/sravya-alla/sets/melody-rnn-results?si=dcf29e0581fe426fa8cc2aba879f9d63&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing

**Full Set of MusicVAE Interpolation Results:** https://soundcloud.com/sravya-alla/sets/musicvae-interpolation?si=e71793eaa1564ebbb96a52d8cb5db7e3&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing
