import numpy as np
import pandas as pd
import time

layer1_clusters_num=12
layer2_clusters_num=6
layer3_clusters_num=4
#layer4_clusters_num=4

with open('../cluster_layers/layer4_cluster_datas_final.csv','w') as fin:
    fin.write("lng,lat,dens,row,col,layer1-cluster,layer2-cluster,layer3-cluster,layer4-cluster,cluster_order_final,center_final_lng,center_final_lat,layer\n")

for layer1_clusters_order in range(0,layer1_clusters_num):
    for layer2_clusters_order in range(0,layer2_clusters_num):
        for layer3_clusters_order in range(0,layer3_clusters_num):
            file_name='../cluster_layers/layer4/layer4_clusters_(layer1-cluster'+str(layer1_clusters_order)+'-layer2-cluster'+str(layer2_clusters_order)+'-layer3-cluster'+str(layer3_clusters_order)+'-dens-1200).csv'
            cluster_datas=pd.read_csv(file_name)
            for i in range(0,cluster_datas.shape[0]):
                with open('../cluster_layers/layer4_cluster_datas_final.csv','a') as fin:
                    fin.write(str(cluster_datas["lng"][i]))
                    fin.write(',')
                    fin.write(str(cluster_datas["lat"][i]))
                    fin.write(',')
                    fin.write(str(cluster_datas["dens"][i]))
                    fin.write(',')
                    fin.write(str(cluster_datas["row"][i]))
                    fin.write(',')
                    fin.write(str(cluster_datas["col"][i]))
                    fin.write(',')
                    fin.write(str(layer1_clusters_order))
                    fin.write(',')
                    fin.write(str(layer2_clusters_order))
                    fin.write(',')
                    fin.write(str(layer3_clusters_order))
                    fin.write(',')
                    fin.write(str(cluster_datas['layer4-cluster'][i]))
                    fin.write(',')
                    fin.write(str(layer1_clusters_order)+str(layer2_clusters_order)+str(layer3_clusters_order)+str(cluster_datas['layer4-cluster'][i]))
                    fin.write(',')
                    fin.write(str(cluster_datas['layer4-center-lng'][i]))
                    fin.write(',')
                    fin.write(str(cluster_datas['layer4-center-lat'][i]))
                    fin.write(',')
                    fin.write(str(4))
                    fin.write('\n')