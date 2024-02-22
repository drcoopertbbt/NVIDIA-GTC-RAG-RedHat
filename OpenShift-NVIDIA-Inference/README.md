# NVIDIA-GTC-RAG-RedHat



```bash
./deploy-only.sh
```


```bash
sudo vim /etc/hosts
```

```bash
10.8.231.15 triton-inference-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com
```

Test Triton Inference Server API health check 

```bash
curl -v http://triton-inference-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com/v2/health/ready
```

Load Models: Triton Inference Server

```bash
curl -X POST http://triton-inference-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com/v2/repository/models/bert/load
```

List Models: Triton Inference Server

```bash
curl -v http://triton-inference-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com/v2/repository/models
```


Unload Models: Triton Inference Server

```bash
curl -X POST http://triton-inference-route-edge-inference.apps.nvd-srv-01.nvidia.eng.rdu2.redhat.com/v2/repository/models/bert/unload
```
