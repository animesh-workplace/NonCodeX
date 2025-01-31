<template>
	<div class="mx-12">
		<div class="flex items-center justify-center w-full">
			<label
				for="dropzone-file"
				class="flex flex-col items-center justify-center w-full h-36 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-200 hover:bg-gray-300"
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

		<div class="flex justify-center align-center my-5" v-if="isUploading">
			<ProgressSpinner class="!w-10 !h-10" strokeWidth="8" fill="transparent" animationDuration="2s" />
		</div>

		<div class="my-12 drop-shadow" v-if="isUploading == false && result.length">
			<div class="flex justify-end">
				<Button label="Download" severity="info" rounded class="mb-8 !px-8" @click="DownloadTable" />
			</div>

			<DataTable
				lazy
				paginator
				:rows="20"
				dataKey="id"
				stripedRows
				:value="result"
				:rowsPerPageOptions="[20, 50, 100, 200, -1]"
			>
				<Column field="chr" header="Chromosome" style="width: 25%"></Column>
				<Column field="start" header="Start" style="width: 25%"></Column>
				<Column field="end" header="End" style="width: 25%"></Column>
				<Column field="type" header="Type" style="width: 25%"></Column>
			</DataTable>
		</div>
	</div>
</template>

<script setup>
import { json2csv } from 'json-2-csv'
import { useQuery } from '@/api/search'

const result = ref([])
const dayjs = useDayjs()
const isUploading = ref(false)

const uploadFile = async (file) => {
	// Validate file type
	if (!file.name.endsWith('.tsv')) {
		throw new Error('Please upload a TSV file')
	}

	const formData = new FormData()
	formData.append('file', file)

	const { uploadQuery } = useQuery()
	try {
		isUploading.value = true
		result.value = await uploadQuery(formData)
		push.success({ title: 'Successfully fetched query' })
		isUploading.value = false
	} catch (err) {
		console.log(err)
		push.error({ title: 'Some error occured' })
	}
}

const handleFileSelect = async (event) => {
	const file = event.target.files[0]
	if (file) {
		try {
			await uploadFile(file)
		} catch (error) {
			console.error('Upload failed:', error)
		}
	}
}

const handleDrop = async (event) => {
	const file = event.dataTransfer.files[0]
	if (file) {
		try {
			await uploadFile(file)
		} catch (error) {
			console.error('Upload failed:', error)
		}
	}
}

const download_blob = (blob, filename) => {
	const link = document.createElement('a')
	link.href = URL.createObjectURL(blob)
	link.download = filename
	document.body.appendChild(link)
	link.click()
	document.body.removeChild(link)
}

const DownloadTable = () => {
	const TableBlob = new Blob([json2csv(result.value, { emptyFieldValue: '', delimiter: { field: '\t' } })], {
		type: 'text/tab-separated-values',
	})
	download_blob(TableBlob, `noncodex_download_table_${dayjs().format('DD_MM_YYYY_hh_mm_a')}.tsv`)
}
</script>

<style scoped></style>
