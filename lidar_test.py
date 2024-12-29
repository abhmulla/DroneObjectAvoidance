from listen_to_lidar import listen_to_lidar

lidar_data, stop = listen_to_lidar()

try:
    while True:
        for angle, dist in lidar_data['distances'].items():
            if dist < 0 or dist > 1200:
                print(f"Invalid distance at angle {angle}: {dist}")
                break
            print("Angle: ", angle, ", Distance: ", dist, "\n")
        print("Properties of data packet")
        data_packet = lidar_data['last_packet_data']
        print('start_angle: ', data_packet.start_angle)
        print('end_angle: ', data_packet.end_angle)
        print('speed: ', data_packet.speed)
        print('time stamp: ', data_packet.time_stamp)
        print('confidence_i (first 5): ', data_packet.confidence_i[:5])
        print('angle_i (first 5): ', data_packet.angle_i[:5])
        print('distance_i (first 5): ', data_packet.distance_i[:5])
except KeyboardInterrupt:
    print("Stopping LiDAR test.")
    stop()  

    