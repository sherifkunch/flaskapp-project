#!/bin/bash

docker pull 392209090241.dkr.ecr.eu-central-1.amazonaws.com/demo-2025:d4c6cc1815d57282365e852a62e0c8728ff14b63

docker run -p 5002:5000 392209090241.dkr.ecr.eu-central-1.amazonaws.com/demo-2025:d4c6cc1815d57282365e852a62e0c8728ff14b63a