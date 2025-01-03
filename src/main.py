#!/usr/bin/env python
from devops.crew import DevopsCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    DevopsCrew().crew().kickoff(inputs=inputs)