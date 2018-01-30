# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..reconst import EstimateFOD


def test_EstimateFOD_inputs():
    input_map = dict(
        algorithm=dict(
            argstr='%s',
            mandatory=True,
            position=-8,
        ),
        args=dict(argstr='%s', ),
        bval_scale=dict(argstr='-bvalue_scaling %s', ),
        csf_odf=dict(
            argstr='%s',
            position=-1,
        ),
        csf_txt=dict(
            argstr='%s',
            position=-2,
        ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        gm_odf=dict(
            argstr='%s',
            position=-3,
        ),
        gm_txt=dict(
            argstr='%s',
            position=-4,
        ),
        grad_file=dict(argstr='-grad %s', ),
        grad_fsl=dict(argstr='-fslgrad %s %s', ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        in_bval=dict(),
        in_bvec=dict(argstr='-fslgrad %s %s', ),
        in_dirs=dict(argstr='-directions %s', ),
        in_file=dict(
            argstr='%s',
            mandatory=True,
            position=-7,
        ),
        mask_file=dict(argstr='-mask %s', ),
        max_sh=dict(argstr='-lmax %d', ),
        nthreads=dict(
            argstr='-nthreads %d',
            nohash=True,
        ),
        shell=dict(
            argstr='-shell %s',
            sep=',',
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        wm_odf=dict(
            argstr='%s',
            mandatory=True,
            position=-5,
            usedefault=True,
        ),
        wm_txt=dict(
            argstr='%s',
            mandatory=True,
            position=-6,
        ),
    )
    inputs = EstimateFOD.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_EstimateFOD_outputs():
    output_map = dict(
        csf_odf=dict(argstr='%s', ),
        gm_odf=dict(argstr='%s', ),
        wm_odf=dict(argstr='%s', ),
    )
    outputs = EstimateFOD.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
