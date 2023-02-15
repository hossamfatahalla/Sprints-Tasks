module "network" {

    source = "./network"
    cidr = var.cidr
    public_subnet_1_cidr= var.public_subnet_1_cidr
    public_subnet_2_cidr= var.public_subnet_2_cidr
    private_subnet_1_cidr= var.private_subnet_1_cidr
    private_subnet_2_cidr= var.private_subnet_2_cidr
    
  
}

module "compute" {

    source = "./compute"
    cidr = var.cidr
    myvpc = module.network.myvpc
    public_subnet_1 = module.network.public_subnet_id_1
    private_subnet_1 = module.network.private_subnet_id_1
    region = var.region
  
}