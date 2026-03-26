<template>
    <UEmpty
      size="lg"
      icon="i-lucide-folders"
      title="No folders found"
      description="Please create a new folder and upload any documents you’d like."
      :actions="[
        {
          icon: 'i-lucide-plus',
          label: 'Create new',
        },
      ]"
    />
</template>

<script setup></script>

<style lang="css" scoped></style>
