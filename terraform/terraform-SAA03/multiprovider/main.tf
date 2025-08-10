terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.5.0"
    }

    google = {
      source  = "hashicorp/google"
      version = "6.45.0"
    }

    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.37.0"
    }
  }
}

provider "aws" {
  # Configuration options
  region = "ap-southeast-1"
}

provider "google" {
  # Configuration options
  region = "ap-southeast-2"
}

provider "azurerm" {
  # Configuration options
  features {

  }
}