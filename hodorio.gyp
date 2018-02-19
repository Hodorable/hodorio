{
  'includes': [
    'build_commons.gypi',
  ],

  # hodorio project
  'targets': [
    {
      'target_name': 'hodorio',
      'type': 'static_library',
      'cflags': [
        '-Werror',
      ],
      'dependencies': [
      ],
      'sources': [
        'include/foo.h',
        
        'src/foo.cpp',
      ],
      'include_dirs': [
         'include',
         'src',
      ],
    },

    # unit test project
    {
      'target_name': 'hodorio_unit_test',
      'type': 'executable',
      'include_dirs': [
        'test/',
      ],
      'sources': [
        'test/test_main.cpp',
      ],
      'dependencies': [
         'hodorio',
       ],
      'conditions':[
       ["OS=='mac'", {
          'include_dirs': [
            'third_part/google_test/include/',
           ],
           'library_dirs': [
             'third_part/google_test/mac_lib/',
            ],
           'libraries': [
            'libgtest.a',
            'libgtest_main.a',
            'libgmock.a',
            'libgmock_main.a',
           ],
         },
        ],
       ],
    },
  ],
}
