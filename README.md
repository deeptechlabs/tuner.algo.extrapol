# Speeding up Automatic Hyperparameter Optimization of Deep Neural Networks by Extrapolation of Learning Curves

By Tobias Domhan, Jost Tobias Springenberg, and Frank Hutter, 2014.
University of Freiburg, Freiburg, Germany
{domhant,springj,fh}@cs.uni-freiburg.de

Experienced human experts in deep learning commonly rely on a large “bag of tricks” to
determine model hyperparameters (Bengio, 2012), as well as learning rates for stochastic
gradient descent (SGD) (LeCun et al., 1998; Bottou, 2012). Using this acquired knowledge
they can often tell after a few SGD iterations whether the training procedure will converge
to a model with competitive performance or not. To save time, they then prematurely
terminate runs expected to perform poorly. Automating this manual trick would be valuable
for speeding up both structure search (Bergstra et al., 2011, 2013; Swersky et al., 2013) and
hyperparameter optimization (Snoek et al., 2012; Eggensperger et al., 2013), which are
currently often prohibitively expensive (Krizhevsky et al., 2012).
We take a first step towards this goal by studying methods for extrapolating from
the first part of a learning curve to its remainder. Preliminary results indicate that such
predictions can be quite accurate and enable the early termination of poor runs.

Copyright by Tobias Domhan, Jost Tobias Springenberg, and Frank Hutter, 2014

Orion Implementation Copyright by Dendi Suhubdy, 2018
