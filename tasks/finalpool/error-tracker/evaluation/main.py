# evaluation script for error-tracker
import os

def evaluate():
    workspace = os.environ.get('WORKSPACE', '.')
    log_file = os.path.join(workspace, 'error_log.json')
    report_file = os.path.join(workspace, 'error_report.md')
    assert os.path.exists(log_file), 'error_log.json not found'
    assert os.path.exists(report_file), 'error_report.md not found'
    print('Evaluation passed')

if __name__ == '__main__':
    evaluate()
