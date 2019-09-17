<h1>Word2Vec</h1>
<ul>
  <li>Word2Vec is one of the emerging and prominent word embedding techniques proposed by Mikolov et al.</li>
  <li>Word2vec is an algorithm that accepts text corpus as an input and outputs a vector representation for each word.</li>
  <li>There are two types of word embedding: <br></li>
  <ol>
    <li> Continuous bag of words (CBOW) </li>
    <li> Skip Gram </li>
  </ol>
</ul>

<h3> Continuous bag of words (CBOW) </h3>
<p>  CBOW finds a target word by given its neighbouring words. Here, a window slides over the text corpus and target words are being predicted. </p>

<h3> Skip Gram </h3>
<p>Skip Gram is opposite to CBOW. Skip Gram taken target value as input and predicted its neighbouring words.</p>
<h3> Dependecies </h3>
<ul>
  <li>This project is tested on CPU Core i5 (6th Gen), 8 GB RAM </li>
  <li>Python  3.6.7 </li>
</ul>
 <h3> Requirements </h3>
 <p>Install requirements packages by the following command <br> </p>
 
  ``` pip install -r requirments.txt ```

<h3> Training Parameters </h3>
<ul>
  <li>sg=0 (sg=0 for CBOW and sg = 1 for Skip Gram) </li>
  <li>Window=10 (window size 10) </li>
  <li>size=300 (Vector Dimension) </li>
</ul>
