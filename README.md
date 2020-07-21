# facebook-toxic-comments-classifier
## **Introduction** <br>
<p align="justify">
The goal of this project is to create a classifier that can predict the toxicity of Facebook comments on Zambian pages. The code was made to be used for general purpose, so it can be applied in whatever topic your project is in as long as it is text related and using facebook comments.
</p> <br>

## **Methodology** <br>
<p align="justify">
The facebook comments were scraped by using a custom Python script which mainly utilised selenium. The comments were scraped by using the HTML class where they where located. These were identified by using chrome developer mode since Google Chrome was the web browser used. Once scraped, the comments were written into a txt file. By using pandas, the comments were preprocessed and transformed in readiness for the trained model. To train the model, a dataset from Google Tensosflow was used. The dataset is civil_comments, this could not be uploaded into the repository due to its size. To train the model, naive bayes multinomial classofoer from sklearn models was used. A detailed report for this project can be emailed to you upon request. <a href = "mailto:mumbiemumbi@icloud.com">mumbiemumbi@icloud.com</a>
</p>

**Files Contained**<br>
<ol>
  <li><strong>fbinfo.py</strong></li>
  &nbsp;&nbsp;&nbsp;&nbsp;<p align="justify"> Python script containing Facebook login details. The information is currently empty for privacy sake.</p>
  <li><strong>fbscrape.py</strong></li>
  &nbsp;&nbsp;&nbsp;&nbsp; <p align="justify">Script used to scrape Facebook comments. Only comment text was scraped. Comments on how to use the code are given.</p>
  <li><strong>Comments_cleaning.ipynb</strong></li>
  &nbsp;&nbsp;&nbsp;&nbsp; <p align="justify">Jupyter notebook used to preprocess the comments.</p>
  <li><strong>Comments_transformation.ipynb</strong></li>
  &nbsp;&nbsp;&nbsp;&nbsp; <p align="justify">Jupyter notebook used to transform text using TF-IDF.</p>
  <li><strong>naive_training.ipynb</strong></li>
  &nbsp;&nbsp;&nbsp;&nbsp; <p align="justify">Jupyter notebook used to preprocess the training dataset and train the model.</p>
  <li><strong>modeled_comments.ipynb</strong></li> 
  &nbsp;&nbsp;&nbsp;&nbsp;<p align="justify">Jupyter notebook where the trained model is deployed on the transformed Facebook comments.</p>
  <li><strong>mwebantu_scraped_comments.txt</strong></li> 
   &nbsp;&nbsp;&nbsp;&nbsp;<p align="justify"> Text file containing all the scraped comments from Zambian Facebook page Mwebantu dated 23 May 2020 which read, <strong>"JUST IN: DORA SILIYA TESTS POSTIVE FOR #COVID-19"</strong>
</ol> 
