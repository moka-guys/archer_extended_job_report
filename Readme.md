# Archer Extended Job Report Scripts
This repo contains scripts provided by Archer to run reports that allow users to export QC data from the Archer software to add to local analysis workbooks.
For information on how to add these scripts to the Archer platform see Archer Analysis Software Management DOC317 in Q-Pulse.

## Extended_Job_Report_Viapath.html.tmpl
This html is used in the archer analysis software to generate extended job reports, which are pdf files generated within the Archer software.

## create_custom_summary_out.py
This python script is added as a Job Hook. When run, this hook will output the data from the Extended Job Report that is required to be copied in to the workbook in .csv format.

## Archer disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.