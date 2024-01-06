# One-KVM-docker
One-KVM，结合廉价硬件和PiKVM，实现低成本远控方案。

使用示例

```docker run -itd -p443:443 -p80:80 --name pikvm-docker --device=/dev/ttyUSB0:/dev/kvmd-hid --device=/dev/video0:/dev/kvmd-video pikvm-ch9329:0.61```