import qiime2.plugin

import {{cookiecutter.package_name}}

# These imports are only included to support the example methods and
# visualizers. Remove these imports when you are ready to develop your plugin.
from q2_dummy_types import IntSequence1, IntSequence2, Mapping
from ._dummy_method import concatenate_ints
from ._dummy_visualizer import mapping_viz

plugin = qiime2.plugin.Plugin(
    name='{{cookiecutter.plugin_name}}',
    version={{cookiecutter.package_name}}.__version__,
    website='{{cookiecutter.url}}',
    package='{{cookiecutter.package_name}}',
    # Information on how to obtain user support should be provided as a free
    # text string via user_support_text. If None is provided, users will
    # be referred to the plugin's website for support.
    user_support_text=None,
    # Information on how the plugin should be cited should be provided as a
    # free text string via citation_text. If None is provided, users
    # will be told to use the plugin's website as a citation.
    citation_text=None
)

# The next two code blocks are examples of how to register methods and
# visualizers. Replace them with your own registrations when you are ready to
# develop your plugin.

plugin.methods.register_function(
    function=concatenate_ints,
    inputs={
        'ints1': IntSequence1 | IntSequence2,
        'ints2': IntSequence1,
        'ints3': IntSequence2
    },
    parameters={
        'int1': qiime2.plugin.Int,
        'int2': qiime2.plugin.Int
    },
    outputs=[
        ('concatenated_ints', IntSequence1)
    ],
    input_descriptions={
        'ints1': 'The first collection of integers to be concatenated.',
        'ints2': 'The second collection of integers to be concatenated.',
        'ints3': 'The third collection of integers to be concatenated.'
    },
    parameter_descriptions={
        'int1': 'The first single integer to be concatenated.',
        'int2': 'The second single integer to be concatenated.'
    },
    output_descriptions={
        'concatenated_ints': 'The resulting concatenated integers.'
    },
    name='Concatenate integers',
    description='This method concatenates integers into a single sequence in '
                'the order they are provided.'
)

plugin.visualizers.register_function(
    function=mapping_viz,
    inputs={
        'mapping1': Mapping,
        'mapping2': Mapping
    },
    parameters={
        'key_label': qiime2.plugin.Str,
        'value_label': qiime2.plugin.Str
    },
    input_descriptions={
        'mapping1': 'The first mapping to be visualized.',
        'mapping2': 'The second mapping to be visualized.'
    },
    parameter_descriptions={
        'key_label': ('The label to include in the visualization for the '
                      'columns containing mapping keys.'),
        'value_label': ('The label to include in the visualization for the '
                        'columns containing mapping values.'),
    },
    name='Visualize two mappings',
    description='This visualizer produces an HTML visualization of two '
                'key-value mappings, each sorted in alphabetical order by key.'
)
