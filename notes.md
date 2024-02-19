# Notes for presentation and paper

The following are notes for the presentation and paper, which come from the creation of the pipeline and our findings from research and trial and error.

Unorganized notes:

- The text extracted alone from each URL is not sufficient, as it may not signify the purpose of the specific endpoint. Ex. the charlotte.edu homepage has a lot of text, but it is not clear what the purpose of the page is. The text is mainly facts about UNCC. To solve this, we can use the title of the page, the URL, and the text to determine the purpose of the page using an LLM model.
- The LLM model can be trained on a dataset of URLs and their purposes. The model can then be used to predict the purpose of a URL. Or we can use a pre-trained model which will likely be sufficient.

# Discoveries

