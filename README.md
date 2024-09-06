已在主仓库实现，推荐使用 https://github.com/mofeng-git/One-KVM 中的 Docker 部署方式，此仓库将会被删除。


# One-KVM-docker
One-KVM，结合廉价硬件和PiKVM，实现低成本远控方案。

使用示例

```docker run -itd -p443:443 -p80:80 --name pikvm-docker --device=/dev/ttyUSB0:/dev/kvmd-hid --device=/dev/video0:/dev/kvmd-video pikvm-ch9329:0.61```
