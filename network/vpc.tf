resource "aws_vpc" "myvpc" {
  cidr_block = var.cidr
  enable_dns_support = "false"
}