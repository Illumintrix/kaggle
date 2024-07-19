{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "16531a0e",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-19T21:50:26.965667Z",
     "iopub.status.busy": "2024-07-19T21:50:26.965206Z",
     "iopub.status.idle": "2024-07-19T21:50:27.973381Z",
     "shell.execute_reply": "2024-07-19T21:50:27.972066Z"
    },
    "papermill": {
     "duration": 1.016174,
     "end_time": "2024-07-19T21:50:27.976001",
     "exception": false,
     "start_time": "2024-07-19T21:50:26.959827",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>StudentID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Ethnicity</th>\n",
       "      <th>ParentalEducation</th>\n",
       "      <th>StudyTimeWeekly</th>\n",
       "      <th>Absences</th>\n",
       "      <th>Tutoring</th>\n",
       "      <th>ParentalSupport</th>\n",
       "      <th>Extracurricular</th>\n",
       "      <th>Sports</th>\n",
       "      <th>Music</th>\n",
       "      <th>Volunteering</th>\n",
       "      <th>GPA</th>\n",
       "      <th>GradeClass</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1001</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>19.833723</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2.929196</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1002</td>\n",
       "      <td>18</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>15.408756</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3.042915</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1003</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4.210570</td>\n",
       "      <td>26</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.112602</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1004</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>10.028829</td>\n",
       "      <td>14</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2.054218</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1005</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>4.672495</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1.288061</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   StudentID  Age  Gender  Ethnicity  ParentalEducation  StudyTimeWeekly  \\\n",
       "0       1001   17       1          0                  2        19.833723   \n",
       "1       1002   18       0          0                  1        15.408756   \n",
       "2       1003   15       0          2                  3         4.210570   \n",
       "3       1004   17       1          0                  3        10.028829   \n",
       "4       1005   17       1          0                  2         4.672495   \n",
       "\n",
       "   Absences  Tutoring  ParentalSupport  Extracurricular  Sports  Music  \\\n",
       "0         7         1                2                0       0      1   \n",
       "1         0         0                1                0       0      0   \n",
       "2        26         0                2                0       0      0   \n",
       "3        14         0                3                1       0      0   \n",
       "4        17         1                3                0       0      0   \n",
       "\n",
       "   Volunteering       GPA  GradeClass  \n",
       "0             0  2.929196         2.0  \n",
       "1             0  3.042915         1.0  \n",
       "2             0  0.112602         4.0  \n",
       "3             0  2.054218         3.0  \n",
       "4             0  1.288061         4.0  "
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd \n",
    "\n",
    "student_data = pd.read_csv(\"/kaggle/input/students/Student_performance_data _.csv\")\n",
    "\n",
    "student_data.head(5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "bef38f6d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-19T21:50:27.985032Z",
     "iopub.status.busy": "2024-07-19T21:50:27.984621Z",
     "iopub.status.idle": "2024-07-19T21:50:27.999478Z",
     "shell.execute_reply": "2024-07-19T21:50:27.998436Z"
    },
    "papermill": {
     "duration": 0.02252,
     "end_time": "2024-07-19T21:50:28.002302",
     "exception": false,
     "start_time": "2024-07-19T21:50:27.979782",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "GradeClass\n",
       "4.0    1211\n",
       "3.0     414\n",
       "2.0     391\n",
       "1.0     269\n",
       "0.0     107\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "New_data = student_data.GradeClass.value_counts()\n",
    "\n",
    "New_data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "075c2c95",
   "metadata": {
    "papermill": {
     "duration": 0.003257,
     "end_time": "2024-07-19T21:50:28.009150",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.005893",
     "status": "completed"
    },
    "tags": []
   },
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "178fec61",
   "metadata": {
    "papermill": {
     "duration": 0.003218,
     "end_time": "2024-07-19T21:50:28.015816",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.012598",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Average Age of the students"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e8d50083",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-19T21:50:28.025045Z",
     "iopub.status.busy": "2024-07-19T21:50:28.024025Z",
     "iopub.status.idle": "2024-07-19T21:50:28.033389Z",
     "shell.execute_reply": "2024-07-19T21:50:28.031851Z"
    },
    "papermill": {
     "duration": 0.016569,
     "end_time": "2024-07-19T21:50:28.035822",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.019253",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "16.468645484949832"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "avg_age = student_data.Age.mean()\n",
    "\n",
    "avg_age"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c20ef199",
   "metadata": {
    "papermill": {
     "duration": 0.00347,
     "end_time": "2024-07-19T21:50:28.043180",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.039710",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Students GPA greater than 3\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "faad49f3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-19T21:50:28.052177Z",
     "iopub.status.busy": "2024-07-19T21:50:28.051789Z",
     "iopub.status.idle": "2024-07-19T21:50:28.067493Z",
     "shell.execute_reply": "2024-07-19T21:50:28.066299Z"
    },
    "papermill": {
     "duration": 0.023055,
     "end_time": "2024-07-19T21:50:28.069890",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.046835",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>StudentID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Ethnicity</th>\n",
       "      <th>ParentalEducation</th>\n",
       "      <th>StudyTimeWeekly</th>\n",
       "      <th>Absences</th>\n",
       "      <th>Tutoring</th>\n",
       "      <th>ParentalSupport</th>\n",
       "      <th>Extracurricular</th>\n",
       "      <th>Sports</th>\n",
       "      <th>Music</th>\n",
       "      <th>Volunteering</th>\n",
       "      <th>GPA</th>\n",
       "      <th>GradeClass</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1001</td>\n",
       "      <td>17</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>19.833723</td>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2.929196</td>\n",
       "      <td>2.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1002</td>\n",
       "      <td>18</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>15.408756</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3.042915</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1003</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>3</td>\n",
       "      <td>4.210570</td>\n",
       "      <td>26</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0.112602</td>\n",
       "      <td>4.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   StudentID  Age  Gender  Ethnicity  ParentalEducation  StudyTimeWeekly  \\\n",
       "0       1001   17       1          0                  2        19.833723   \n",
       "1       1002   18       0          0                  1        15.408756   \n",
       "2       1003   15       0          2                  3         4.210570   \n",
       "\n",
       "   Absences  Tutoring  ParentalSupport  Extracurricular  Sports  Music  \\\n",
       "0         7         1                2                0       0      1   \n",
       "1         0         0                1                0       0      0   \n",
       "2        26         0                2                0       0      0   \n",
       "\n",
       "   Volunteering       GPA  GradeClass  \n",
       "0             0  2.929196         2.0  \n",
       "1             0  3.042915         1.0  \n",
       "2             0  0.112602         4.0  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student_data.head(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "2f1dcbd2",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-19T21:50:28.079574Z",
     "iopub.status.busy": "2024-07-19T21:50:28.079207Z",
     "iopub.status.idle": "2024-07-19T21:50:28.092401Z",
     "shell.execute_reply": "2024-07-19T21:50:28.091282Z"
    },
    "papermill": {
     "duration": 0.021034,
     "end_time": "2024-07-19T21:50:28.094936",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.073902",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(321, 15)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "student_GPA3 = student_data[student_data.GPA > 3].shape\n",
    "\n",
    "student_GPA3"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8605a19b",
   "metadata": {
    "papermill": {
     "duration": 0.004007,
     "end_time": "2024-07-19T21:50:28.103149",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.099142",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Find the top 5 students with the highest GPA & then age to break the tie"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "40a28c1d",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2024-07-19T21:50:28.113121Z",
     "iopub.status.busy": "2024-07-19T21:50:28.112720Z",
     "iopub.status.idle": "2024-07-19T21:50:28.139830Z",
     "shell.execute_reply": "2024-07-19T21:50:28.138693Z"
    },
    "papermill": {
     "duration": 0.035068,
     "end_time": "2024-07-19T21:50:28.142468",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.107400",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>StudentID</th>\n",
       "      <th>Age</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Ethnicity</th>\n",
       "      <th>ParentalEducation</th>\n",
       "      <th>StudyTimeWeekly</th>\n",
       "      <th>Absences</th>\n",
       "      <th>Tutoring</th>\n",
       "      <th>ParentalSupport</th>\n",
       "      <th>Extracurricular</th>\n",
       "      <th>Sports</th>\n",
       "      <th>Music</th>\n",
       "      <th>Volunteering</th>\n",
       "      <th>GPA</th>\n",
       "      <th>GradeClass</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1919</th>\n",
       "      <td>2920</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>17.442121</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1278</th>\n",
       "      <td>2279</td>\n",
       "      <td>15</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>18.899696</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>442</th>\n",
       "      <td>1443</td>\n",
       "      <td>15</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>19.424398</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2028</th>\n",
       "      <td>3029</td>\n",
       "      <td>16</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>18.656924</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2319</th>\n",
       "      <td>3320</td>\n",
       "      <td>17</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>2</td>\n",
       "      <td>9.285447</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>3.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      StudentID  Age  Gender  Ethnicity  ParentalEducation  StudyTimeWeekly  \\\n",
       "1919       2920   15       0          3                  1        17.442121   \n",
       "1278       2279   15       1          0                  2        18.899696   \n",
       "442        1443   15       0          0                  2        19.424398   \n",
       "2028       3029   16       1          0                  0        18.656924   \n",
       "2319       3320   17       0          0                  2         9.285447   \n",
       "\n",
       "      Absences  Tutoring  ParentalSupport  Extracurricular  Sports  Music  \\\n",
       "1919         1         1                1                1       1      0   \n",
       "1278         3         1                3                1       1      0   \n",
       "442          0         0                3                0       1      1   \n",
       "2028         0         1                4                1       0      0   \n",
       "2319         0         0                4                1       0      1   \n",
       "\n",
       "      Volunteering  GPA  GradeClass  \n",
       "1919             0  4.0         0.0  \n",
       "1278             0  4.0         0.0  \n",
       "442              1  4.0         0.0  \n",
       "2028             1  4.0         0.0  \n",
       "2319             1  4.0         3.0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Top_students = student_data.sort_values(by = ['GPA','Age', 'StudyTimeWeekly'], ascending = [False, True, True])\n",
    "\n",
    "Top_students = Top_students.head(5)\n",
    "Top_students"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ed0deba",
   "metadata": {
    "papermill": {
     "duration": 0.004167,
     "end_time": "2024-07-19T21:50:28.151482",
     "exception": false,
     "start_time": "2024-07-19T21:50:28.147315",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "none",
   "dataSources": [
    {
     "datasetId": 5417270,
     "sourceId": 8993808,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 30746,
   "isGpuEnabled": false,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 4.678544,
   "end_time": "2024-07-19T21:50:28.678367",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2024-07-19T21:50:23.999823",
   "version": "2.5.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
