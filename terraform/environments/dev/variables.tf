variable "aws_region" {
  description = "AWS region for the OpsFabric environment"
  type        = string
  default     = "us-east-1"
}

variable "environment" {
  description = "Deployment environment"
  type        = string
  default     = "dev"
}

variable "project_name" {
  description = "Project name used for AWS resource naming and tagging"
  type        = string
  default     = "opsfabric"
}