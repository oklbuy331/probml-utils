import pytest
import probml_utils as pml


def test_import_scripts():
    # Files
    pml.__version__
    pml.savefig
    pml.latexify
    pml.hinton_diagram
    pml.plot_ellipse
    pml.convergence_test
    pml.kdeg
    pml.scale_3d
    pml.style3d


def test_import_modules():
    from probml_utils import fisher_lda_fit
    from probml_utils import gauss_utils
    from probml_utils import gmm_lib
    from probml_utils import mix_bernoulli_lib
    from probml_utils import mixture_lib
    from probml_utils import pgmpy_utils
    from probml_utils import plotting
    from probml_utils import prefit_voting_classifier
    from probml_utils import pyprobml_utils
    from probml_utils import rvm_classifier, rvm_regressor
