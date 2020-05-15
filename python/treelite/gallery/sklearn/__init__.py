# coding: utf-8

from .common import SKLConverterBase
from .gbm_regressor import SKLGBMRegressorMixin
from .gbm_classifier import SKLGBMClassifierMixin
from .gbm_multi_classifier import SKLGBMMultiClassifierMixin
from .rf_regressor import SKLRFRegressorMixin
from .rf_classifier import SKLRFClassifierMixin
from .rf_multi_classifier import SKLRFMultiClassifierMixin


def import_model(sklearn_model):
    """
    Load a tree ensemble model from a scikit-learn model object

    Parameters
    ----------
    sklearn_model : object of type \
                    :py:class:`~sklearn.ensemble.RandomForestRegressor` / \
                    :py:class:`~sklearn.ensemble.RandomForestClassifier` / \
                    :py:class:`~sklearn.ensemble.GradientBoostingRegressor` / \
                    :py:class:`~sklearn.ensemble.GradientBoostingClassifier`
        Python handle to scikit-learn model

    Returns
    -------
    model : :py:class:`~treelite.Model` object
        loaded model

    Example
    -------

    .. code-block:: python
      :emphasize-lines: 8

      import sklearn.datasets
      import sklearn.ensemble
      X, y = sklearn.datasets.load_boston(return_X_y=True)
      clf = sklearn.ensemble.RandomForestRegressor(n_estimators=10)
      clf.fit(X, y)

      import treelite.gallery.sklearn
      model = treelite.gallery.sklearn.import_model(clf)
    """
    class_name = sklearn_model.__class__.__name__
    module_name = sklearn_model.__module__.split('.')[0]

    if module_name != 'sklearn':
        raise Exception('Not a scikit-learn model')

    if class_name == 'RandomForestRegressor':
        return SKLRFRegressorConverter.process_model(sklearn_model)
    elif class_name == 'RandomForestClassifier':
        if sklearn_model.n_classes_ == 2:
            return SKLRFClassifierConverter.process_model(sklearn_model)
        elif sklearn_model.n_classes_ > 2:
            return SKLRFMultiClassifierConverter.process_model(sklearn_model)
        else:
            raise Exception('n_classes_ must be at least 2')
    elif class_name == 'GradientBoostingRegressor':
        return SKLGBMRegressorConverter.process_model(sklearn_model)
    elif class_name == 'GradientBoostingClassifier':
        if sklearn_model.n_classes_ == 2:
            return SKLGBMClassifierConverter.process_model(sklearn_model)
        elif sklearn_model.n_classes_ > 2:
            return SKLGBMMultiClassifierConverter.process_model(sklearn_model)
        else:
            raise Exception('n_classes_ must be at least 2')
    else:
        raise Exception('Unsupported model type: only '
                        'random forests and gradient boosted trees are supported')


class SKLGBMRegressorConverter(SKLGBMRegressorMixin, SKLConverterBase):
    pass


class SKLGBMClassifierConverter(SKLGBMClassifierMixin, SKLConverterBase):
    pass


class SKLGBMMultiClassifierConverter(SKLGBMMultiClassifierMixin, SKLConverterBase):
    pass


class SKLRFRegressorConverter(SKLRFRegressorMixin, SKLConverterBase):
    pass


class SKLRFClassifierConverter(SKLRFClassifierMixin, SKLConverterBase):
    pass


class SKLRFMultiClassifierConverter(SKLRFMultiClassifierMixin, SKLConverterBase):
    pass


__all__ = ['import_model']
