# Machine-Learning-Notes

## Supervised Machiene Learning
Thus far supervised machine learning has gained the most traction in use cases across business applications. Studying labeled data, these techniques can extend patterns to unlabeled data.

Supervised learning is used for many business applications from spam filters to movie recommendations. We looked at the two broad categories of supervised machine learning: <br>
<ul>
  <li>Classification</li>
  <li>Regression</li>
</ul> 

Deep learning can be used within supervised machine learning to create techniques that are better at image recognition or identifying when a movie was created based on the video footage.


## Unsupervised Machine Learning
Unsupervised techniques are the second most used in business applications. By learning patterns even when data do not have labels, these techniques can group items together that are likely to be similar.


Unsupervised techniques are used for business applications from figuring out market segments to again building recommendation engines. There are a lot of ways you can build recommendation engines! But more of that will be shown in term 2.

These two techniques (supervised and unsupervised) will be the main techniques focused on in this term. You will also use deep learning as a supervised learning technique for image recognition.

## Reinforcement Learning
The final type of machine learning, reinforcement learning, has recently been gaining a lot of traction, but still is limited in its use cases related to many business use cases. There are a number of obstacles in training these algorithms, and the approaches are not as streamlined as the other approaches you will see in this term.

With that being said, recent publicity in reinforcement learning has come from AlphaGo and autonomous vehicles. Additionally, reinforcement learning is often used in gaming agents like you see in Open AI Gym.



# Support Vector Machines Recap
SVMs are a popular algorithm used for classification problems. You saw three different ways that SVMs can be implemented:
<ul>
  <li>Maximum Margin Classifier</li>
  <li>Classification with Inseparable Classes</li>
  <li>Kernel Methods</li>
</ul>

## Maximum Margin Classifier
When your data can be completely separated, the linear version of SVMs attempts to maximize the distance from the linear boundary to the closest points (called the support vectors). For this reason, we saw that in the picture below, the boundary on the left is better than the one on the right.

![screen-shot-2018-06-02-at-5 34 36-pm](https://user-images.githubusercontent.com/78471151/147876947-c5099857-7b5a-4d7e-b6ad-06dddae45750.png)


## Classification with Inseparable Classes
Unfortunately, data in the real world is rarely completely separable as shown in the above images. For this reason, we introduced a new hyper-parameter called C. The C hyper-parameter determines how flexible we are willing to be with the points that fall on the wrong side of our dividing boundary. The value of C ranges between 0 and infinity. When C is large, you are forcing your boundary to have fewer errors than when it is a small value.

Note: when C is too large for a particular set of data, you might not get convergence at all because your data cannot be separated with the small number of errors allotted with such a large value of C.

![screen-shot-2018-06-02-at-5 52 44-pm](https://user-images.githubusercontent.com/78471151/147876968-e0eb5e61-86ce-4a42-b02b-75895a531174.png)

## Kernels
Finally, we looked at what makes SVMs truly powerful, kernels. Kernels in SVMs allow us the ability to separate data when the boundary between them is nonlinear. Specifically, you saw two types of kernels:
<ul>
  <li>polynomial</li>
  <li>rbf</li>
</ul>

By far the most popular kernel is the rbf kernel (which stands for radial basis function). The rbf kernel allows you the opportunity to classify points that seem hard to separate in any space. This is a density based approach that looks at the closeness of points to one another. This introduces another hyper-parameter gamma. When gamma is large, the outcome is similar to having a large value of C, that is your algorithm will attempt to classify every point correctly. Alternatively, small values of gamma will try to cluster in a more general way that will make more mistakes, but may perform better when it sees new data.

![screen-shot-2018-06-02-at-6 07 54-pm](https://user-images.githubusercontent.com/78471151/147877029-0c3e204f-6189-4a85-a722-736c978c1f3d.png)



