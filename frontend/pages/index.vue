<template>
	<div class="mx-12">
		<div class="flex items-center justify-center w-full">
			<label
				for="dropzone-file"
				class="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-200 hover:bg-gray-300"
				@dragover.prevent
				@drop.prevent="handleDrop"
			>
				<div class="flex flex-col items-center justify-center pt-5 pb-6">
					<svg
						class="w-8 h-8 mb-4 text-gray-500"
						aria-hidden="true"
						xmlns="http://www.w3.org/2000/svg"
						fill="none"
						viewBox="0 0 20 16"
					>
						<path
							stroke="currentColor"
							stroke-linecap="round"
							stroke-linejoin="round"
							stroke-width="2"
							d="M13 13h3a3 3 0 0 0 0-6h-.025A5.56 5.56 0 0 0 16 6.5 5.5 5.5 0 0 0 5.207 5.021C5.137 5.017 5.071 5 5 5a4 4 0 0 0 0 8h2.167M10 15V6m0 0L8 8m2-2 2 2"
						/>
					</svg>
					<p class="mb-2 text-gray-500">
						<span class="font-semibold">Click to upload</span> or drag and drop
					</p>
					<p class="text-sm text-gray-500">Only TSV file</p>
				</div>
				<input id="dropzone-file" type="file" class="hidden" accept=".tsv" @change="handleFileSelect" />
			</label>
		</div>
	</div>
</template>

<script setup>
import { useQuery } from '@/api/search'
const errorMessage = ref('')

const uploadFile = async (file) => {
	// Validate file type
	if (!file.name.endsWith('.tsv')) {
		throw new Error('Please upload a TSV file')
	}

	const formData = new FormData()
	formData.append('file', file)

	const { uploadQuery } = useQuery()
	try {
		await uploadQuery(formData)
		push.success({
			title: 'Successfully Uploaded',
			message: 'Starting Analysis',
		})
	} catch (err) {
		console.log(err)
	}
}

const handleFileSelect = async (event) => {
	const file = event.target.files[0]
	if (file) {
		try {
			errorMessage.value = ''
			const result = await uploadFile(file)
			console.log('Upload successful:', result)
			// You can emit an event here to notify parent component
			// emit('upload-success', result)
		} catch (error) {
			errorMessage.value = error.message
			console.error('Upload failed:', error)
			// emit('upload-error', error)
		}
	}
}

const handleDrop = async (event) => {
	const file = event.dataTransfer.files[0]
	if (file) {
		try {
			errorMessage.value = ''
			const result = await uploadFile(file)
			console.log('Upload successful:', result)
			// emit('upload-success', result)
		} catch (error) {
			errorMessage.value = error.message
			console.error('Upload failed:', error)
			// emit('upload-error', error)
		}
	}
}
</script>

<style scoped></style>
