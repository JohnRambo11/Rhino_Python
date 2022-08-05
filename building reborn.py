#coding=utf-8
import rhinoscriptsyntax as rs
# import datetime

# 自动对每一帧导出图片
def render_step(render_folder,sequence_number):
    file_name = str(int(sequence_number)).zfill(5)
    file_path = " " + render_folder + file_name + ".png"
    # enter之前加空格
    rs.Command("_-ViewCaptureToFile" + file_path + " _Enter")

def output():
    # 输出文件夹
    render_folder = "D:\\Python\\RhinoPython\\practice\\output5\\"    
    groupList = []
    numGroup = rs.GetInteger("选择要参与生成的群组数量")
    for step in range(numGroup):
        step = rs.GetObjects("select the objects_group")
        groupList.append(step)
        rs.HideObjects(step)
    for i in range(len(groupList)):
        group = groupList[i]
        # 对每一个群组做一个逐渐飞入效果
        rs.MoveObject(group,(0,0,100000))
        rs.ShowObject(group)
        for j in range(40):           
            rs.MoveObject(group,(0,0,-2500))
            render_step(render_folder,(i*100000+j))

        # 对每一个群组的物件做循环，挨个生成每个图元
        # for k in range(len(group)):
        #     rs.ShowObject(group[k])
        #     if k % 100 == 0:
        #         render_step(render_folder,(i*100000+k))
        
def main():   
    output()

main()