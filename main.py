import os

def create_folders(base_path, folder_structure):
    for folder, subfolders in folder_structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        if subfolders:
            create_folders(folder_path, subfolders)

def create_file_structure_txt(base_path):
    file_structure_txt = """root/
│
├── public/
│   ├── assets/
│   │   ├── images/ - Stores all image files
│   │   │   ├── logos/ - Stores logo images
│   │   │   ├── icons/ - Stores icon images
│   │   │   └── ... - Additional image folders
│   │   ├── fonts/ - Stores font files
│   │   │   ├── custom/ - Custom fonts
│   │   │   └── webfonts/ - Web fonts
│   │   ├── videos/ - Stores video files
│   │   ├── audio/ - Stores audio files
│   │   └── documents/ - Stores document files
│   ├── css/ - Stores CSS files
│   ├── js/ - Stores JavaScript files
│   └── ... - Additional public folders
│
├── src/
│   ├── controllers/ - Stores controller files
│   ├── models/ - Stores model files
│   ├── views/ - Stores view files
│   │   ├── layouts/ - Layout files for views
│   │   ├── partials/ - Partial view files
│   │   │   ├── header/ - Header partials
│   │   │   ├── footer/ - Footer partials
│   │   │   └── ... - Additional partials
│   │   └── pages/ - Page view files
│   ├── styles/ - Stores style files
│   │   ├── base/ - Base styles
│   │   ├── components/ - Component styles
│   │   ├── layouts/ - Layout styles
│   │   └── pages/ - Page-specific styles
│   ├── utils/ - Utility functions
│   ├── services/ - Service files
│   └── ... - Additional source folders
│
├── assets/
│   ├── database/ - Database files
│   └── documentation/ - Documentation files
│       ├── file_structure.txt - Overview of the file structure
│       └── ... - Additional documentation
│
├── scripts/ - Stores scripts
│
└── ... - Additional root folders
"""
    documentation_path = os.path.join(base_path, 'assets', 'documentation')
    os.makedirs(documentation_path, exist_ok=True)
    with open(os.path.join(documentation_path, 'file_structure.txt'), 'w', encoding='utf-8') as f:
        f.write(file_structure_txt)

def main():
    base_path = os.getcwd()

    folder_structure = {
        'public': {
            'assets': {
                'images': {
                    'logos': {},
                    'icons': {},
                    '...': {}
                },
                'fonts': {
                    'custom': {},
                    'webfonts': {},
                },
                'videos': {},
                'audio': {},
                'documents': {}
            },
            'css': {},
            'js': {},
            '...': {}
        },
        'src': {
            'controllers': {},
            'models': {},
            'views': {
                'layouts': {},
                'partials': {
                    'header': {},
                    'footer': {},
                    '...': {}
                },
                'pages': {}
            },
            'styles': {
                'base': {},
                'components': {},
                'layouts': {},
                'pages': {}
            },
            'utils': {},
            'services': {},
            '...': {}
        },
        'assets': {
            'database': {},
            'documentation': {
                '...': {}
            }
        },
        'scripts': {},
        '...': {}
    }

    create_folders(base_path, folder_structure)
    create_file_structure_txt(base_path)
    print("Web development project folder layout created successfully!")

if __name__ == "__main__":
    main()
