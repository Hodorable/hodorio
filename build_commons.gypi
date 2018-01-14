{
  'target_defaults': {
    # default CFLAGS for all platform and all target
    'cflags': [
      '-Wall',
      '-fPIC',
    ],
    # CFLAGS for all target in mac, for xcode won't read the 'cflags'
    'include_dirs': [
      '.',
    ],
    'conditions': [
      ['OS=="mac"', {
         'xcode_settings': {
           'CLANG_CXX_LANGUAGE_STANDARD': 'c++0x',
           'WARNING_CFLAGS': [
             '-Wall',
             '-Wno-deprecated-declarations',
           ],
           'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
         },
        'defines': [
          'HODORIO_POSIX',
        ],
      }],
    ]
  }
}
