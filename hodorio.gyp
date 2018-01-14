{
  'includes': [
    'build_commons.gypi',
  ],
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
    }
  ],
}
