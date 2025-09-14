# Task 003: Kubernetes Cluster Configuration Analysis

## Problem Statement
Analyze a production Kubernetes cluster configuration including all components, security policies, and operational procedures.

## Requirements

### Primary Objectives
1. **Cluster Architecture**
   - Document namespace organization and resource isolation
   - Analyze deployment strategies and replica management
   - Map service discovery and networking configuration
   - Assess ingress controllers and load balancing setup

2. **Security & Access Control**
   - Review RBAC policies and service accounts
   - Analyze network policies and security contexts
   - Document secret management and encryption
   - Assess pod security policies and admission controllers

3. **Resource Management**
   - Analyze resource requests, limits, and quotas
   - Document auto-scaling configurations (HPA, VPA, CA)
   - Review storage classes and persistent volume management
   - Assess node affinity and scheduling policies

### Technical Focus Areas
- **Workload Management**: Deployments, StatefulSets, DaemonSets, Jobs
- **Networking**: Services, Ingress, NetworkPolicies, CNI configuration
- **Storage**: PersistentVolumes, StorageClasses, CSI drivers
- **Monitoring**: Prometheus, Grafana, logging aggregation
- **Security**: Pod Security Standards, OPA Gatekeeper, Falco

### Deliverables
- Cluster architecture diagram with all components
- Security assessment report with compliance gaps
- Resource utilization analysis and optimization recommendations
- Operational procedures and troubleshooting guide
- Disaster recovery and backup strategy documentation

### Success Criteria
- Complete inventory of all cluster resources
- Clear understanding of security posture
- Actionable optimization recommendations
- Comprehensive operational documentation

### Complexity: Advanced
**Skills Required:** Kubernetes, container orchestration, security, networking
**Estimated Time:** 4-5 hours
**Agent Coordination:** K8s specialist + Security analyst + Operations engineer
