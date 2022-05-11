variable "meraki_api" {}
variable "vmx_serial" {}

provider "aws" {
  region="us-east-1"
}

terraform {
  required_providers {
    http-full = {
      source = "salrashid123/http-full"
    }
  }
}

provider "http-full" {}

data "http" "vmx_token" {
  provider = http-full
  url = "https://api.meraki.com/api/v1/devices/${var.vmx_serial}/appliance/vmx/authenticationToken"

  method = "POST"

  request_headers = {
    Content-Type = "application/json",
    X-Cisco-Meraki-API-Key = "${var.meraki_api}"
  }
}

resource "aws_vpc" "vmx_vpc" {
  cidr_block           = "10.1.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true
  tags = {
    Name = "vmx_vpc"
  }
}

resource "aws_subnet" "vmx_subnet" {
  vpc_id                   = aws_vpc.vmx_vpc.id
  cidr_block               = "10.1.0.0/24"
  availability_zone        = "us-east-1a"
  tags = {
    Name = "vmx_subnet"
  }
}

resource "aws_internet_gateway" "inet_gw" {
  vpc_id = aws_vpc.vmx_vpc.id
}

resource "aws_route_table" "vmx_rt" {
  vpc_id = aws_vpc.vmx_vpc.id
  tags = {
    Name = "vmx_rt"
  }
}

resource "aws_route_table_association" "vmx_rt_assoc" {
  subnet_id = aws_subnet.vmx_subnet.id
  route_table_id = aws_route_table.vmx_rt.id
}

resource "aws_route" "vmx_rt_dfgw" {
  route_table_id = aws_route_table.vmx_rt.id
  destination_cidr_block = "0.0.0.0/0"
  gateway_id = aws_internet_gateway.inet_gw.id
}

resource "aws_security_group" "all_access" {
  vpc_id = aws_vpc.vmx_vpc.id
  name = "all-access-vmx"
  tags = {
    Name = "all-access-vmx"
  }
  egress = [
    {
      description = "Allow all outbound"
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []
      prefix_list_ids = []
      security_groups = []
      self = false
    }
  ]
   ingress = [
    {
      description = "Allow all inbound"
      from_port = 0
      to_port = 0
      protocol = "-1"
      cidr_blocks = ["0.0.0.0/0"]
      ipv6_cidr_blocks = []
      prefix_list_ids = []
      security_groups = []
      self = false
    }
  ]
}

data "aws_ami" "ami_vmx" {
  most_recent = true
  owners = ["679593333241"]
  filter {
    name = "name"
    values = ["vmx-15*"]
  }
  filter {
    name = "product-code"
    values = ["3b9cqpv3g20ug18amhpumu8et"]
  }
}

resource "aws_instance" "vmx" {
  ami = data.aws_ami.ami_vmx.id
  instance_type = "m4.large"
  source_dest_check = false
  associate_public_ip_address = true
  user_data = jsondecode(data.http.vmx_token.body)["token"]
  subnet_id = aws_subnet.vmx_subnet.id
  vpc_security_group_ids = [aws_security_group.all_access.id]
  tags = {
    Name = "vmx"
  }
}
