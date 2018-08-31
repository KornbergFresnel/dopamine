"""Management file:

1) generate new algorithm directory under `dopamine/agents`
2) render rapidly
"""

import sys
import os
import argparse

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# if __name__ == '__main__':
#     os.environ.setdefault('DOPAMINE_SETTINGS_MODULE', 'settings')
#     try:
#         from tools.management import execute_from_command_line
#     except ImportError as exec:
#         raise ImportError(
#             "Couldn't import Dopamine."
#         ) from exec
#     execute_from_command_line(sys.argv)
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--create_algo', type=str, 
                        help='Create new algorithm basement, there will create a sub-directory under `dopamine/agents`')
    parser.add_argument('--delete_algo', type=str,
                        help='Delete an old algorithm basement from `dopamine/agents`')
    args = parser.parse_args()

    if args.create_algo is not None:
        # TODO: check legality
        dir_path = os.path.join(BASE_DIR, 'dopamine/agents', args.create_algo)
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            raise Exception('This algorithm exists, please try another name or check the path: `{}`'.format(dir_path))
        else:
            print('--- Creating new algorithm basement ...')
            os.mkdir(dir_path)
            os.mkdir(os.path.join(dir_path, 'configs'))
            with open(os.path.join(dir_path, 'configs', '%s.gin' % args.create_algo), 'w') as f: pass
            with open(os.path.join(dir_path, '__init__.py'), 'w') as f: pass
            with open(os.path.join(dir_path, '%s_agent,py' % args.create_algo), 'w') as f: pass
            print('--- `%s` has been created!' % args.create_algo)
    
    if args.delete_algo is not None:
        algo_name = args.delete_algo
        dir_path = os.path.join(BASE_DIR, 'dopamine/agents', algo_name)
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            import shutil
            shutil.rmtree(dir_path)
        else:
            raise Exception('`%s` does not exist or not a directory, please check again!')
        
            
        