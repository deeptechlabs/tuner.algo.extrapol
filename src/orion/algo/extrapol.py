# -*- coding: utf-8 -*-
"""
:mod:`orion.algo.extrapol` -- Perform extrapolation of learning curves
================================================================================

.. module:: extrapol
   :platform: Unix
   :synopsis: Use extrapolation of learning curves to save computational 
              resources to find the best set of hyperparameters

"""
import numpy

from orion.algo.base import BaseAlgorithm

from .curvefunctions import  all_models, model_defaults
from .curvemodels import CurveModel, MLCurveModel, LinearCurveModel
from .curvemodels import masked_mean_x_greater_than

class ExtrapolatingLearningCurves(BaseAlgorithm):
    """Implement extrapolating learning curves algorithm."""

    def __init__(self, space, dx_tolerance=1e-7):
        """Declare `learning_rate` as a hyperparameter of this algorithm."""
        super(ExtrapolatingLearningCurves, self).__init__(space,
                                               dx_tolerance=dx_tolerance,
                                               type='Linear')
        self.has_observed_once = False
        self.current_point = None
        if type == 'Linear':
            self.model = LinearCurveModel()
        else:
            if model_name in model_defaults:
                self.model = MLCurveMovel(function=all_models[model_name],
                             default_vals=model_defaults[model_name],
                             recency_weighting=True)
            else:
                self.model = MLCurveMovel(function=all_models[model_name], recency_weighting=True)
        
        self.prob_greater_types = ["posterior_mean_prob_x_greater_than",
                              "posterior_prob_x_greater_than"]

        self.model_name_types = ["pow3", "log_power"]

    def suggest(self, num=1, std=0.01):
        """Suggest a `num`ber of new sets of parameters.

        Perform suggestion of points from curve extrapolation

        """
        assert num >= 1 
        if not self.has_observed_once:
            return self.space.sample(1)
        
        self.current_point -= self.learning_rate * self.gradient
        
        #generate some data for the model
        params = self.model.default_function_param_array()
        params =  params + np.random.rand(params.shape[0])
        self.current_point = self.model.function(space, *params)
        self.current_point += std*np.random.randn(y.shape[0])
        return [self.current_point]

    def observe(self, points, results):
        """Observe evaluation `results` corresponding to list of `points` in
        space.

        Save current point corresponding to this point.

        """
        self.current_point = numpy.asarray(points[-1])
        self.has_observed_once = True

    @property
    def is_done(self, xlim=500, num_train=200):
        """
            The termination criterion expects the learning_curve in a file
            called learning_curve.txt as well as the current best value in 
            ybest.txt. We create both files and see if the termination
            criterion correctly predicts to cancel or continue running
            under various artificial ybest.
        """

        for prob_x_greater_type in self.prob_greater_types:
            # generate some data:
            for model_name in self.model_name_types:
                function = all_models[model_name]
                params = model_defaults[model_name]
                x = np.arange(1, xlim, 1)
                y = function(x, **params)
                noise = 0.0005 * np.random.randn(len(y))
                y_noisy = y + noise
                y_final = y_noisy[-1]
                np.savetxt("./learning_curve.txt", y_noisy[:200])
                write_xlim(xlim)

                print("Actual ybest: %f" % y_noisy[-1])

                # we set ybest to be higher than the final value of this curve
                # hence we DO want the evaluation to stop!
                # TODO: adjust this to send to database instead
                open("./ybest.txt", "w").write(str(y_final + 0.05))
                open("./termination_criterion_running", "w").write("running")

                ret = main(mode="conservative",
                    prob_x_greater_type=prob_x_greater_type,
                    nthreads=4)

                self.assertTrue(os.path.exists("./y_predict.txt"))
                y_predict = float(open("./y_predict.txt").read())
                abserr = np.abs(y_predict - y_noisy[-1])
                print("abs error %f" % abserr)

                #we set ybest to be lower than the final value of this curve
                #hence we DON'T want the evaluation to stop!
                # TODO: adjust this to send to database instead
                open("./ybest.txt", "w").write(str(y_final - 0.05))
                open("./termination_criterion_running", "w").write("running")

                ret = main(mode="conservative",
                    prob_x_greater_type=prob_x_greater_type,
                    nthreads=4)
        
        return ret == 0
