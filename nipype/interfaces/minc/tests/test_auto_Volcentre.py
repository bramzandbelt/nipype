# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..minc import Volcentre


def test_Volcentre_inputs():
    input_map = dict(
        args=dict(argstr='%s', ),
        centre=dict(argstr='-centre %s %s %s', ),
        clobber=dict(
            argstr='-clobber',
            usedefault=True,
        ),
        com=dict(argstr='-com', ),
        environ=dict(
            nohash=True,
            usedefault=True,
        ),
        ignore_exception=dict(
            deprecated='1.0.0',
            nohash=True,
            usedefault=True,
        ),
        input_file=dict(
            argstr='%s',
            mandatory=True,
            position=-2,
        ),
        output_file=dict(
            argstr='%s',
            genfile=True,
            hash_files=False,
            name_source=['input_file'],
            name_template='%s_volcentre.mnc',
            position=-1,
        ),
        terminal_output=dict(
            deprecated='1.0.0',
            nohash=True,
        ),
        verbose=dict(argstr='-verbose', ),
        zero_dircos=dict(argstr='-zero_dircos', ),
    )
    inputs = Volcentre.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_Volcentre_outputs():
    output_map = dict(output_file=dict(), )
    outputs = Volcentre.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
