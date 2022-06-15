#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Hook to extra and sort pre-defined values from the "Summary.r_and_d_results.txt" file.

@author: urs.lahrmann@invitae.com
@version: 20220614
@customer: www.viapath.co.uk

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
import logging
import pandas as pd
from argparse import ArgumentParser

# row order to use for sorting
CUSTOM_ROW_ORDER = [
    "MOLBAR_TOTAL_NUM_READS",
    "MOLBAR_READS_WITH_CORRECT_COMMON_REGION",
    "RAW_FRAGMENT_TOTAL",
    "RAW_FRAGMENT_FILTERED_ON_TARGET_PERCENT",
    "UNIQUE_FRAGMENT_FILTERED_ON_TARGET_PERCENT",
    "AVERAGE_UNIQUE_RNA_START_SITES_PER_CONTROL_GSP2",
    "UNIQUE_RNA_FRAGMENT_MEAN_LENGTH"
    ]

def runHook(job_dir, hook_out):
    """
    Re-sort summary r_and_d file.

    Parameters
    ----------
    job_dir : str
        The main directory of the analysis job
    hook_out : str
        The output directory for hooks in Archer Analysis

    Returns
    -------
    None.

    """
    # enable logging
    logging.basicConfig(
        filename=os.path.join(hook_out, "hook_resort_randd.log"),
        encoding='utf-8',
        level=logging.DEBUG)

    randd_file = os.path.join(job_dir, "summaries", "Summary.r_and_d_results.txt")
    if not os.path.exists(randd_file):
        logging.error("Error - File not found: {}".format(randd_file))
    else:
        logging.info("Found summaries file.")
        logging.debug("Row order: {}".format(CUSTOM_ROW_ORDER))
    pddf = pd.read_csv(randd_file, sep="\t", index_col=0)
    logging.info("Compare pre-defined row names with the ones in summary file")
    input_names = set(pd.DataFrame(pddf).index)
    reference_names = set(CUSTOM_ROW_ORDER)
    if len(reference_names) != len(CUSTOM_ROW_ORDER):
        logging.warning("Warning: Reference list contains duplicated records")
    if reference_names - input_names:
        logging.warning("Warning: The reference contains records that are not in the input!")
        logging.debug("ref-in: {}".format(reference_names - input_names))
    if input_names - reference_names :
        logging.info("Info: The input contains records that are not in the reference - This is probably intended behaviour for this hook!")
        logging.debug("in-ref: {}".format(input_names - reference_names))
    if not reference_names ^ input_names:
        logging.info("Reference and input content matches. All good! :)")
    # do the actual re-sorting
    pddf = pddf.reindex(CUSTOM_ROW_ORDER)
    pddf.to_csv(os.path.join(hook_out, "Summary.r_and_d_results.mod.txt"), sep="\t")


def main():
    """
    Argument handling and start of processing.

    Returns
    -------
    None.

    """
    parser = ArgumentParser(description='')
    parser.add_argument(
        "-d", "--job_dir",
        required=True,
        help="Job directory")
    parser.add_argument(
        "-o", "--output",
        required=True,
        help="Hook output directory")

    args = parser.parse_args()
    runHook(
        args.job_dir,
        args.output)

if __name__ == "__main__":
    main()
