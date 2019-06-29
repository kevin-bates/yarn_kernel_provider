"""Provides support for launching and managing kernels within a YARN cluster."""

from remote_kernel_provider.provider import RemoteKernelProviderBase


class YarnKernelProvider(RemoteKernelProviderBase):
    id = 'yarn'
    lifecycle_manager_class = 'yarn_kernel_provider.yarn.YarnLifecycleManager'
